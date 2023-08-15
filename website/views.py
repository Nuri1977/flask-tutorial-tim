from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
from .models import Note
from .database import db


views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html", user = current_user)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        data = request.form.get('data')

        if len(data) < 2:
            flash('Note is too short!', category='error')
        else:
            newNote = Note(data=data, user_id=current_user.id)
            db.session.add(newNote)
            db.session.commit()
            flash('Note added!', category='seccess')
        
        # Redirect to the GET route after processing the form submission
        return redirect(url_for('views.notes'))

    return render_template("notes.html", user = current_user)