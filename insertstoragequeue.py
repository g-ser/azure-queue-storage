import uuid
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient

default_credential = DefaultAzureCredential()
# account_url = "https://<YOUR_STORAGE_ACCOUNT_NAME>.queue.core.windows.net"
account_url = "https://storageaccountsummer.queue.core.windows.net"
queue_name = "quickstartqueues-" + str(uuid.uuid4())


try:
    print("Azure Queue storage - Insert messages to storage queue")
    # Create queue client and queue
    queue_service = QueueServiceClient(account_url, default_credential)
    # Create queue
    queue = queue_service.create_queue(queue_name)
    # Send first message to queue
    queue.send_message(u"First message")
    # Send second message to queue
    queue.send_message(u"Second message")
    # Send third message to queue
    queue.send_message(u"Third message")
except Exception as ex:
    print('Exception:')
    print(ex)

