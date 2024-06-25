#!/usr/bin/env python3

from flask import Flask,Response

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_string(parameter):
    print(parameter)
    return f'{parameter}'

@app.route('/count/<int:parameter>')
def count(parameter):
    result = ''
    for num in range(parameter):
        result += f'{num}\n'
    
    return result, 200, {'Content-Type': 'text/plain'}

         

@app.route('/math/<int:num>/<operation>/<int:num2>')
def math(num,operation,num2):
    if operation =='+':
        value =str( num + num2)
        return value
    elif operation =='-':
        value =str( num - num2)
        return value
    elif operation =='*':
        value =str( num*num2)
        return value
    elif operation in ['div','/']:
        value =str( num /num2)
        return value
    elif operation =='%':
        value =str( num % num2)
        return value
    return value
if __name__ == '__main__':
    app.run(port=5555, debug=True)
