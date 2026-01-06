from locust import HttpUser, task, between

class HelloWorldUser(HttpUser):
    wait_time = between(0.0, 0.0)

    @task
    def hello(self):
        self.client.get("/")
