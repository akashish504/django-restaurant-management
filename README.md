This is a repo to be used in order management in a pizzeria.

There is no dockerisation available. In the next update, dockersation will be available.

The stack used here is python-django-rest, mysql, celery, rabbitmq,

`To read the code, instructions are given in the last part of this file.`


### This service has three parts.
1. Database Engine - This part deals with the mysql database. We are using mySQL here.
2. Backend Engine - This part deals with the API engine for the service. 
3. Task Scheduler - This part deals with the changing of status of ongoing order. This task scheduler actually has two parts a `message-broker` and a `task-queue`.





## Database Engine
We are using mySQL here as database service. To run install and run mysql locally you can use `brew` command or using package installer. Anyways start the mysql service in background.



## Backend Engine

To start the backend engine first create a python virtual environment and source the environment.

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Then from the root directory install the required modules.

```bash
pip install -r requirements.txt
```

Now you can start your backend server but before that you need to run migrations scripts in order to create database schemas in your database.
To do that run these commands.

```bash
python manage.py makemigrations
python manage.py migrate
```

Now we are ready and running the below command should start your backend service.
```bash
python manage.py runserver
```

## Tash Scheduler

For this task scheduler first you need to start a message broker. You can use rabbitmq, redis or anything broker of your choice. Rabbitmq ahs been used here. Now installing and running rabbit-mq is same as mysql. You can use `brew` commands to do so.

For next task, this is to run a message queue, python-celery has been used here. You can use the same virtual environment as you used in the backend service to run this service.

To run this service just type below command in the shell.

```bash
celery -A tasks worker -l INFO 
```

This should our scheduler service. 



# Final Service

Now to interact with our final service two endpoint have been exposed. 

1. ### To create orders.

```bash
curl --location 'http://localhost:8000/api/placeOrder/' \
--header 'Content-Type: application/json' \
--data '{
    "pizza": [
        {
            "base": "pan pizza",
            "cheese": "mozerella",
            "customer_name": "customer_3",
            "table_number": 1,
            "order_status": "Accepted",
            "description": "this is a test order"
        },
        {
            "base": "cheese burst",
            "cheese": "cheddar",
            "customer_name": "customer_2",
            "table_number": 7,
            "order_status": "Accepted",
            "description": "this is a test order"
        }
    ]
}'
```

Using above API you can place order for pizza.


2. ### To track certain order

```bash
curl --location 'http://localhost:8000/api/orderStatus/?order_id=8'
```

To trigger this API we need to pass order ID as query param.


# Main Part of Code

To read the code-base you can refer to 2 key places.
1. `tasks.py` - To know more about the celery workers.
2. `./apis` - To know more about APIs, models, etc.
