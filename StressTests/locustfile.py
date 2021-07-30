import gevent
from locust import HttpUser, task, between
from locust.env import Environment
from locust.stats import stats_printer, stats_history
from locust.log import setup_logging

setup_logging("INFO", None)


class User(HttpUser):
    host = "http://127.0.0.1:5000/"

    @task(500)
    def task_1(self):
        self.client.get("/push?value=32")

    @task(500)
    def task_2(self):
        self.client.get("/pop")
    @task(1)
    def task_3(self):
        self.client.get("/max")


# setup Environment and Runner
env = Environment(user_classes=[User])
env.create_local_runner()


# start a greenlet that periodically outputs the current stats
gevent.spawn(stats_printer(env.stats))

# start a greenlet that save current stats to history
gevent.spawn(stats_history, env.runner)

# start the test
env.runner.start(10000000, spawn_rate=10000)

# in 60 seconds stop the runner
gevent.spawn_later(60, lambda: env.runner.quit())

# wait for the greenlets
env.runner.greenlet.join()

