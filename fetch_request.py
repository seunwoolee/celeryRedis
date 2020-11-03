import requests
from requests import Response

from celery_config import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def fetch_url(url):
    result: Response = requests.get(url)
    return result.status_code