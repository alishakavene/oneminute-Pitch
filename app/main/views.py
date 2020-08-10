from flask import render_template,redirect,url_for,abort
from . import main
from ..models import User,Pitch
from .forms import UpdateProfile,PitchForm
from .. import db
from django.contrib.auth.decorators import login_required

# Views
@main.route('/')
def index():
    pitches = Pitch.all_pitches()
    title = 'Pitch - Pitch Website'
    return render_template('index.html',title = title, pitches = pitches)

@main.route('/pitch/<pitch_id>')
def pitch (pitch_id):
    
    return render_template('pitch.html', id = pitch_id)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/pitch/new/',methods = ['GET','POST'])
@login_required
def  new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        
        new_pitch = Pitch(pitch_title=title, pitch_content=pitch,
                          category=category, user=current_user, likes=0, dislikes=0)

        # Save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.index'))

    title = 'New pitch'
    return render_template('new_pitch.html', title=title, form = form)