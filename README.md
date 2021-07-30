# App:
The app folder contains the first task, which is the Stack as a Service.  <br />
It is also deployed online using Heroku at https://viastackkirilspiridonov.herokuapp.com/ <br />
Locally you can use the `server_start.bat` file to run the server or using you python IDE and running `wsgi.py`.

# Stress Tests
The StressTests folder contains a folder with manual python scripts for the required stress test and `locust.py` file,
which is a library for stress/load testing an API. The first test *'Measure the time of pushing 10M integeres, and then poping them to empty stack.'*
may take up to 2 hours to complete, that is why there are two versions of this stress test - a slower and a faster version, respectively `LoadTest_SLOWER.py`
and `LoadTest_FASTER.py` <br /><br />
The other file `locustfile.py` is a loadtesting file using  [Locust](https://docs.locust.io/en/stable/what-is-locust.html). It does not answer directly to the questions asked in the *Stress Test* tab,
but provides a useful statistics about our app and makes load/stress testing easier.


