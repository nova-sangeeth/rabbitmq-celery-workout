from celery.worker import celery_app
import logging

logger = logging.getLogger(__name__)


def testing():
    try: 
        logger.info('testing inside 1')
        route = celery_app.amqp.routes[0].route_for_task("worker.test_celery")
        task_1 = celery_app.send_task("worker.test_celery_2")
        logger.debug(task_1)
    except:
        logger.info('testing inside failed')
    return None


testing()