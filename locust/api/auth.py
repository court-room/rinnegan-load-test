from locust import HttpUser
from locust import between
from locust import task


class AuthAPI(HttpUser):
    wait_time = between(1, 2)
    HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

    @task
    def sign_up(self):
        pass

    @task
    def sign_in(self):
        pass

    @task
    def refresh(self):
        pass

    def on_start(self):
        pass
