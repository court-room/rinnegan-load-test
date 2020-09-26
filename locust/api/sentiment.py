from locust import HttpUser
from locust import between
from locust import task


class SentimentAPI(HttpUser):
    wait_time = between(1, 2)
    HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

    def on_start(self):
        pass
