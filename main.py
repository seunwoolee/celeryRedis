from celery.result import AsyncResult

from fetch_request import fetch_url
from tasks import add

if __name__ == "__main__":

    print('@@')
    for url in ["http://google.com", "https://amazon.in", "https://facebook.com", "https://twitter.com", "https://alexa.com"]:
        result: AsyncResult = fetch_url.delay(url)
        print(result.get())
        print(result.state)

    print('!!')