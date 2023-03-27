from flask import render_template, session,flash,redirect, request
import re
from flask_bcrypt import Bcrypt
from flask_app import app
from flask_app.models.model_user import User
from flask_app.models.model_listing import listing
from flask_app.models.model_message import Message

@app.route('/message/<int:id>')
def message(id):
    id={
        'id':id
    }
    return render_template('message.html',listing= listing.get_by_id(id) )



@app.route('/post_message',methods=['POST'])
def post_message():

    if 'user_id' not in session:
        return redirect('/')

    Message.save(request.form)

    return redirect('/inbox')

@app.route('/destroy/message/<int:message_id>')
def destroy_message(message_id):

    Message.destroy(message_id)

    return redirect('/inbox')