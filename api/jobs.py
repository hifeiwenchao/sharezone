from sharezone import celery_app
from api import service

import logging
logger = logging.getLogger('api')


@celery_app.task(bind=True)
def test(self):
    logger.info('test is running...')


@celery_app.task(bind=True)
def close_order(self, order_id):
    return service.trade.close_order(order_id)
