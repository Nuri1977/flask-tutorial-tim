from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_required, current_user
from .models import Note
from .extensions import db
from flask_login import current_user

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

@views.route('/delete-notes/<id>', methods=['POST'])
def delete_note(id):
    print(id)
    note = Note.query.get(id)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return redirect(url_for('views.notes'))

@views.route('/edit_note/<int:note_id>', methods=['GET', 'POST', 'PUT'])
@login_required
def edit_note(note_id):
    if request.method == 'GET':
        note = Note.query.get(note_id)
        if note:
            if note.user_id == current_user.id:
                return render_template('edit_note.html', note=note, user=current_user)
            flash('Permission denied.', category='error')
        flash('Note not found.', category='error')
        return redirect(url_for('views.notes'))
    
    elif request.method == 'POST':
        note = Note.query.get(note_id)
        if note:
            if note.user_id == current_user.id:
                edited_data = request.form.get('edited_data')
                if len(edited_data) < 2:
                    flash('Note is too short!', category='error')
                else:
                    note.data = edited_data
                    db.session.commit()
                    flash('Note updated!', category='success')
                return redirect(url_for('views.notes'))
            flash('Permission denied.', category='error')
        flash('Note not found.', category='error')
        return redirect(url_for('views.notes'))

