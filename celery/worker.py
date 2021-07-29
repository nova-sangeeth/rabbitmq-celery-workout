from celery import Celery
from kombu import Queue
import logging

logger = logging.getLogger(__name__)
celery_app = Celery("worker", broker="amqp://guest@localhost//")
celery_app.conf.task_always_eager = True
celery_app.conf.timezone = 'UTC'


celery_app.conf.task_routes = {
    "app.worker.test_celery": "main-queue",
    "app.worker.test_celery": "second-queue",
}



@celery_app.task()
def test_celery():
    logger.info("test task return")
    return f"test task return"

    
@celery_app.task()
def test_celery_2():
    logger.info("test task return--------------------")
    return f"test task return"
