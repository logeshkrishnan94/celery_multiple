from __future__ import absolute_import

from celery import Celery
from celery.app.registry import TaskRegistry
from celery_module.celery_task_class import baseclass
from celery_module.config import Config


registry = TaskRegistry()
for model in Config.models:
    registry.register(baseclass(problem=model["problem"]))


app = Celery("celery_module",
            broker="redis://", #redis://192.168.38.6:6379/0
            backend="redis://",
            tasks=registry)

if __name__ == '__main__':
    app.start()
