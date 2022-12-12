from locust import HttpUser, task

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        # self.client.get("/questions/")
        self.client.get("/search/?q=ab")