from flask_app import app
from flask import render_template, session, request, redirect, flash
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
import pprint
from flask_app.models.model_listing import listing












@app.route('/new_show', methods=['POST'])
def create_show():
    data = {
        'title' : request.form['title'],
        'network' : request.form['network'],
        'date' : request.form['date'],
        'description' : request.form['description'],
        'users_id' : session['user_id']
    }
    valid=show.is_valid(data)
    if valid:
        show.create_show(data)
        pprint.pprint(data)
        flash('show added')
        return redirect('/dashboard')
    return redirect('/new')

@app.route('/view/<int:id>')
def view(id):
    id={
        'id':id
    }
    
    return render_template('/view.html',show= show.get_by_id(id),shows= show.get_alls() )

@app.route('/edit/<int:id>' )
def edit(id):
    id={
        'id':id
    }
    
    return render_template('/edit.html',show= show.get_by_id(id))

@app.route('/update', methods=["POST"])
def update():
        show.update(request.form)
        return redirect("/dashboard")

@app.route('/destroy/<int:id>')
def destroy(id):
    data= {
    'id':id
    }
    show.destroy(data)
    return redirect ('/dashboard')