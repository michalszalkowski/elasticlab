import threading
import urllib.request
import urllib.parse
from random import randint
from time import sleep


def worker_xss():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/?type=XSS%20attack%20detect',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_login():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/?type=Login',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_login_fail():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/?type=LoginFail',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_logout():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/?type=Logout',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_sql():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/?type=SqlInjection%20attack%20detect',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_csrf():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/?type=CSRF',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_message_error():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/message/?message=ERROR',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


def worker_message_warn():
    while True:
        req = urllib.request.Request(
            'http://localhost:8090/message/?message=WARN',
            method='GET'
        )
        urllib.request.urlopen(req)
        sleep(randint(1, 5))


t1 = threading.Thread(target=worker_xss)
t1.start()

t2 = threading.Thread(target=worker_login)
t2.start()

t3 = threading.Thread(target=worker_logout)
t3.start()

t4 = threading.Thread(target=worker_sql)
t4.start()

t5 = threading.Thread(target=worker_csrf)
t5.start()

t6 = threading.Thread(target=worker_login_fail)
t6.start()

t7 = threading.Thread(target=worker_message_error)
t7.start()

t8 = threading.Thread(target=worker_message_warn)
t8.start()
