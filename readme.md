# ChatIW Bot
A script that lets you advertise anything you want automatically on [ChatIW](https://chatiw.com/)

## Installation

Requires [Django](https://www.djangoproject.com/) to work.

```sh
$ git clone {link}
$ cd ChatIW-Bot
$ pip install -r requirements.txt
```

Put the [2CaptchaAPI](https://2captcha.com/2captcha-api) key, Text, and Profile Name in the automate.py file

```sh
$ python Automate.py
```

# Multi-Threading
Right now multi-threading is not implemented. You could simply use the Python [Threading](https://docs.python.org/3/library/threading.html) module to implement it.

You could also send headless to True in line 10 and run the script multiple times at once.

