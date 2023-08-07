import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient

default_credential = DefaultAzureCredential()
account_url = "https://storageaccountsummer.queue.core.windows.net"
queue_name = "quickstartqueues-" + str(uuid.uuid4())
queues = []


try:
    print("Azure Queue storage - Read messages from storage Queue")
    # Create queue client
    queue_service = QueueServiceClient(account_url, default_credential)
    
    # Create a list with the names of the queues
    list_queues = queue_service.list_queues()
    for queue in list_queues:
       queues.append(queue.name)
    
    # Get the queue client to interact with the first queue of the list
    myqueue = queue_service.get_queue_client(queue=queues[0])
    
    # Get the length of the queue
    properties = myqueue.get_queue_properties()
    count = properties.approximate_message_count
    
    # Get the content of each message and then delete the message
    messages = myqueue.receive_messages(max_messages=count)

    print("\nPress Enter key to 'process' messages and delete them from the queue...")
    input()

    for msg_batch in messages.by_page():
        for msg in msg_batch:
            # "Process" the message
            print(msg.content)
            # Let the service know we're finished with
            # the message and it can be safely deleted.
            myqueue.delete_message(msg)

    # Delete the queue
    print("\nPress Enter key to delete the queue...")
    input()

    # Clean up
    print("Deleting queue...")
    myqueue.delete_queue()
    
except Exception as ex:
    print('Exception:')
    print(ex)