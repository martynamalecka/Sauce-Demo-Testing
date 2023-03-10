# Sauce Demo Automated Testing

### About
This project validates some functionalities of the https://www.saucedemo.com/ web application.
It consists of several web automation tests created using Python and Selenium.

### Test cases
All test cases can be found here --> 
[Test Cases Google Drive Spreadsheet](https://docs.google.com/spreadsheets/d/1GFpBQruvFGvVo0OABA_7POPHzwcpdI9wrMrJXRe1P7I/edit?usp=sharing)

### Installation
1. Ideally create a new virtual environment.
2. Install all packages according to the configuration file --> requirements.txt.
```commandline 
pip install -r requirements.txt
```
```commandline 
pip install -r requirements-dev.txt
```

### How to run it?
Run all tests in the default Chrome browser.
```commandline
python -m unittest 
```
To run all tests in the Edge or Firefox browser, first set the environment variable.
```commandline
export BROWSER="chrome"
```
Run tests in the Firefox browser.
```commandline
BROWSER=firefox python -m unittest 
```
Run tests in the Edge browser.
```commandline
BROWSER=edge python -m unittest 
```

### Black 
Black Python code auto-formatter has been used in this project.

How to run it?
```commandline
black {source_file_or_directory}
```

### Isort 
Isort formatter has been used in this project to sort imports alphabetically, and automatically separate them into sections and by type.

How to run it?
```commandline
isort {source_file_or_directory}
```