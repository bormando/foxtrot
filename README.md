# Foxtrot
This project is a part of my portfolio. Here you can find UI tests, developed using stack:
- Python (programming language)
- PyTest (test framework for Python)
- Selenium (framework for web automation)
- Docker (isolated environment for test runs)
- Allure (post-test reporting tool)

### How to run these tests?
You'll need to install Python 3.7+ and all packages from "requirements.txt" file:
> pip install -r requirements.txt

Also you'll need to install **Allure-CLI** (and **Java**) if you'd like to generate Allure report.
You can run tests in cloud or on your local/virtual machine, if there's **Docker** and **docker-compose** installed.

Run this command inside project's root directory:
> docker-compose up -d

This commant will start docker-container with Chrome browser inside.

After that, run next command in project's root directory:
> pytest -v -s -m="smoke" --alluredir="allure-results"
