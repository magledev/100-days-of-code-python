from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_goodbye():
    return "Bye"

if __name__ == "__main__":
    app.run()

# Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function
#
# inner_function = outer_function()
# inner_function()

# Python decorator functions
# import time
#
#
# def delay_decorator(function):
#     def wrapper_function():
#         time.sleep(2)
#         function()
#     return wrapper_function
#
# @delay_decorator
# def say_hello():
#     print("Hello")
# @delay_decorator
# def say_goodbye():
#     print("Goodbye")
#
# def say_greeting():
#     print("How are you?")
#
# # say_hello()
# # say_goodbye()
# # say_greeting()
#
# decorated_function = delay_decorator(say_greeting)
# decorated_function()
