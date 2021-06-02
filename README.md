# Test for Tensor


### Install and run:

1. Install [chromedriver](https://chromedriver.chromium.org/) before run test
    
2. Install the requirements.txt file:
```sh
pip install -r requirements.txt
```

3. Install [Allure Framework](https://docs.qameta.io/allure/)

4. Run tests:
```sh
pytest --alluredir=reports
```

5. Run allure report:
```sh
allure serve reports/
```