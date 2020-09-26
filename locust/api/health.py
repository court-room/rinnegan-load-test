from locust import HttpUser
from locust import between
from locust import task


class HealthAPI(HttpUser):
    wait_time = between(1, 2)
    HEADERS = {"Content-Type": "application/json"}

    @task
    def health_check(self):
        self.client.get("/health", headers=self.HEADERS)