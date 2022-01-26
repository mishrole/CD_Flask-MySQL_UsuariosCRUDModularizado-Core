from flask import Flask, render_template, request, redirect
from users_app import app
from users_app.models.userModel import User

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('404.html'), 404

@app.route('/', methods=['GET'])
def index():
    return redirect('/users')

@app.route('/users', methods=['GET'])
def list():
    users = User.get_all()
    return render_template('list.html', users = users)

@app.route('/users/new', methods=['GET'])
def form():
    return render_template('index.html')

@app.route('/users/show/<int:id>', methods=['GET'])
def show(id):
    data = {
        "userId": id
    }

    user = User.findById(data)
    return render_template('show.html', user = user);

@app.route('/users/edit/<int:id>', methods=['GET'])
def edit(id):
    data = {
        "userId": id
    }

    user = User.findById(data)
    return render_template('edit.html', user = user);

# Formulario Crear Usuario
@app.route('/create_user', methods=['POST'])
def create_user():
    data = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"]
    }

    user = User.save(data)

    if user:
        return redirect(f'/users/show/{user}')
    else:
        return redirect('/users')

# Formulario Editar Usuario
@app.route('/edit_user/<int:id>', methods=['POST'])
def edit_user(id):
    user = User.findById({"userId": id})

    if user:
        data = {
            "userId": id,
            "firstname": request.form["firstname"],
            "lastname": request.form["lastname"],
            "email": request.form["email"]
        }

        User.update(data)
        return redirect(f'/users/show/{id}')
    else:
        return redirect('/users')

# Formulario Eliminar Usuario
@app.route('/users/<int:id>/destroy', methods=['POST'])
def delete_user(id):
    data = {
        "userId": id
    }

    user = User.findById(data)

    if user:
        User.delete(data)

    return redirect('/users')