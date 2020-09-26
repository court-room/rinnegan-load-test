from locust import HttpUser
from locust import between
from locust import task


class UserAPI(HttpUser):
    wait_time = between(1, 2)
    HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

    @task
    def get_all_users(self):
        pass

    @task
    def get_a_user(self):
        pass

    @task
    def remove_a_user(self):
        pass

    @task
    def update_a_user(self):
        pass

    def on_start(self):
        pass
