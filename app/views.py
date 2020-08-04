from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    title = 'Galore - Pitch Website'
    return render_template('index.html',title = title)

@app.route('/pitch/<pitch_id>')
def pitch (pitch_id):
    
    return render_template('pitch.html', id = pitch_id)
