from celery_config import app


@app.task
def add(x, y):
    print('###')
    return x + y
