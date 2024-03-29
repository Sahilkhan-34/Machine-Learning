"""
that API endpoint will hit any webbrowser to get the result
If you see any application amazon/gmail all are http url
These http urls create  by web framworks
POSTMAN is an application to test these urls working or not

"""


# def greet():
#     print("Hello World Welcome")

# greet()

# import flask
from flask import Flask, request

# create flask app
app = Flask(__name__) # double underscore