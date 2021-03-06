from flask import Flask, request

from . import Stack as st

app = Flask(__name__)

# Identifying stack at the beginning of the app, as this let us run it without a database and still use memory.
stack = st.Stack()


@app.route("/")
def home():
    return "<h1>Stack API by Kiril Spiridonov</h1><p>This site is a prototype API</p>"


@app.route("/pop", methods=['GET'])
def pop():
    poped_value = stack.pop()
    if poped_value == "Empty Stack":
        return "Record not found", 400
    else:
        return str(poped_value)


@app.route("/push")
def push():
    if 'value' in request.args:
        value = int(request.args['value'])
        stack.push(value)
        return f'Pushed {value}'

    else:
        return "Error: No value field provided. Please specify a value."


@app.route("/max", methods=['GET'])
def max():
    return str(stack.max())
