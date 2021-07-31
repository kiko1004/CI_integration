# App:
The app folder contains the first task, which is the Stack as a Service.  <br />
It is also deployed online using Heroku at https://viastackkirilspiridonov.herokuapp.com/ <br />
Locally you can use the `server_start.bat` file to run the server or using your python IDE and running `wsgi.py`.

# Stress Tests
The StressTests folder contains a folder with manual python scripts for the required stress tests and `locust.py` file,
which is a library for stress/load testing an API. The first test *'Measure the time of pushing 10M integers, and then poping them to empty stack.'*
may take up to 2 hours to complete. That is why there are two versions of this stress test - a slower and a faster version, respectively `LoadTest_SLOWER.py`
and `LoadTest_FASTER.py` <br /><br />
The other file `locustfile.py` is a loadtesting file using  [Locust](https://docs.locust.io/en/stable/what-is-locust.html). It does not answer directly to the questions asked in the *Stress Test* tab,
but provides a useful statistics about our app and makes load/stress testing easier. Preferable way to use it: 
1. Run `server_start.bat`
2. Run `start_locust.bat`

# CI/CD Integration
For Continuous Integration is used a open-source hosted distributed continuous integration service 
called [Travis](https://travis-ci.com/). The corresponding file is `.travis.yml`. The tool is very easy to use and suitable most
programming languages. You should receive an email after any error that occurred.

# Bandit (linter focused on Security)

[Bandit](https://bandit.readthedocs.io/en/latest/) is a great open-source tool that finds common security issues in Python code.
You can run Bandit using `bandit_execute.bat`.
