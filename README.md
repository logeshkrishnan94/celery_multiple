## Activate virtualenv

```virtualenv venv3 --python=python3```\
```source venv3/bin/activate```\
```pip install -r requirements.txt```

# Celery multiple tasks example

Module Structure:

celery_module - Module containing task, celery app (needed to initiate celery worker) and config

    __init__.py (created to avoid celery app import issue)

    celery_app.py (app initiation, broker and backend, task registration)

    celery_task_class.py (Task class definition)
    
    config.py (models for task registration)

celery_test.py (client test function to send input, get output)

## To run the example

* Start redis server for backend and broker using docker

```docker run -d -p 6379:6379 redis```

```redis-cli```

```ping``` -> PONG

* Run the following command from the root folder to start the celery worker

```celery -A celery_module worker --loglevel=INFO --pool threads```

* Run the following command from the root folder to get the predictions

```python celery_test.py```
