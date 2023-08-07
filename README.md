## Content of repo

This repo has two simple python code files:

* ```insertstoragequeue.py```: Creates and populates a queue in a Storage Account (Storage Account must be already created)
* ```readfromstoragequeue.py```: Reads & deletes the messages of the queue, before deletes the queue itself

## Install required python packages

Run the command below using CLI

```shell
pip install -r requirements.txt
```

## Run the app

Open a command prompt that has Python in its path, and then run the code to create the queue and send messages to it:

```shell
python insertstoragequeue.py 
```

When the command above is finished, run the command below to read the content of each message of the queue, delete the messages and finally delete the queue

```shell
python readfromstoragequeue.py
```