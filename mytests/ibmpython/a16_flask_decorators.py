# Server.py
from flask import Flask, render_template, request
from Maths.mathematics import summation, subtraction, multiplication
# Import the Maths package here

app = Flask("Mathematics Problem Solver")

@app.route("/sum")
def sum_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return summation(num1, num2)

@app.route("/sub")
def sub_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return subtraction(num1, num2)

@app.route("/mul")
def mul_route():
    num1 = float(request.args.get('num1'))
    num2 = float(request.args.get('num2'))
    return multiplication(num1, num2) 

@app.route("/")
def render_index_page():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)



# In Maths/__init__.py
# from . import mathematics


# in Maths/mathematics.py
# def summation(a, b):
#     result = a + b
#     return result

# def subtraction(a, b):
#     result = a - b
#     return result

# def multiplication(a, b):
#     result = a * b
#     return result

