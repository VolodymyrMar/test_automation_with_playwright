# Playwright automation with python
Test project to show
    - features of MS Playwright on Python
    - automation project structure using pytest

## Tools:
- [Playwright](https://playwright.dev/python/)
- [Pytest](https://docs.pytest.org/en/6.2.x/)
- [PyCharm](https://www.jetbrains.com/ru-ru/pycharm/)


## Install guide
1. Install python
2. install PyCharm
3. Install python dependencies pip install -r requirements.txt
4. Make sure playwright version 1.8+ installed


## Project structure
- *confitest.py* file contains main fixtures to work
- Page object stored in page_object folder
- Test stored in test folder
- Settings are spread between:
  - pytest.ini
  - settings.py


##   Run guide
1. Create file secure.json for login and passwords. Structure:
```python
    {
    "login": "login",
    "password": "password"
    }
```
2. Install software to test Test-Me
3. Run Test-Me(check quide in it`s repo)
4. Run test using command *pytest*

