''' Decorator example '''

def jsonify_decorator(function):
    ''' Decorator '''
    def modify_output():
        return {"output":function()}
    return modify_output

@jsonify_decorator
def hello():
    ''' Function modified with Decorator '''
    return 'hi world'

@jsonify_decorator
def add():
    ''' Function modified with Decorator '''
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)

print(hello())
print(add())

# @app.route("/userdetails/<userid>")
# def getUserDetails(userid):
#     return "User Details for  "+userid