from flask import Blueprint, render_template, request, flash, jsonify
#This basically defines that this file is the blueprint of our application, 
# it has all the required routes defined here.
from flask_login import login_required, current_user
from .models import Note
from . import db
import json


views = Blueprint('views', __name__)

#Now we write '@' then the name of our blueprint, and then '.route' and 
# inside bracket we give the route
@views.route('/', methods=['GET', 'POST'])
@login_required
def home(): #this function will run whenever we go to the above route 
    if request.method == 'POST':
        note = request.form.get('note')
        
        if len(note) < 1:
            flash('Note is too small.', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    
    return render_template("home.html", user = current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})