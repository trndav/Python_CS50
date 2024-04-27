
# Login
# <form method="POST" action="/login">
#     <input type="text" name="username">
#     <input type="password" name="password">
#     <input type="submit" value="Submit">
# </form>

# from flask import request
# @app.route('/login', methods=['POST'])
# def login():
#     username = request.form['username']
#     password = request.form['password']
#     # process login here

#Login
# from flask import redirect
# @app.route('/admin')
# def admin():
#     return redirect('/login')

# Redirect
# from flask import url_for
# @app.route('/admin')
# def admin():
#     return redirect(url_for('login'))
# @app.route('/login')
# def login():
#     return "<Login Page>"


# POST GET IF
# @app.route('/data', methods=['GET', 'POST'])
# def data():
#     if request.method == 'POST':
#         # process POST request
#     if request.method == 'GET':
#         # process GET request

# <!-- For POST -->
# <form method="POST" action="/data">
#     <!-- Your input fields here -->
#     <input type="submit" value="Submit">
# </form>
# <!-- For GET -->
# <a href="/data">Fetch data</a>


# CRUD Create
# <form method="POST" action="/create">
#     <input type="text" name="name">
#     <input type="submit" value="Create">
# </form>

# @app.route('/create', methods=['GET', 'POST'])
# def create():
#     if request.method == 'POST':
#         # Access form data
#         name = request.form['name']
#         # Create a new record with the name
#         record = create_new_record(name)  # Assuming you have this function defined
#         # Redirect user to the new record
#         return redirect(url_for('read', id=record.id))
#     # Render the form for GET request
#     return render_template('create.html')

# CRUD READ
# @app.route('/read/<int:id>', methods=['GET'])
# def read(id):
#     # Get the record by id
#     record = get_record(id)  # Assuming you have this function defined
#     # Render a template with the record
#     return render_template('read.html', record=record)


# CRUD Update
# <form method="POST" action="/update/{{record.id}}">
#     <input type="text" name="name" value="{{record.name}}">
#     <input type="submit" value="Update">
# </form>

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update(id):
#     if request.method == 'POST':
#         # Access form data
#         name = request.form['name']
#         # Update the record with the new name
#         update_record(id, name)  # Assuming you have this function defined
#         # Redirect user to the updated record
#         return redirect(url_for('read', id=id))
    
#     # Render the form for GET request with current data
#     record = get_record(id)  # Assuming you have this function defined
#     return render_template('update.html', record=record)

# CRUD Delete
# <form method="POST" action="/delete/{{record.id}}">
#     <input type="submit" value="Delete">
# </form>

# @app.route('/delete/<int:id>', methods=['POST'])
# def delete(id):
#     # Delete the record
#     delete_record(id)  # Assuming you have this function defined
#     # Redirect user to the homepage
#     return redirect(url_for('home'))