from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch ', validators=[Required()])
    category = StringField( 'Category', validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

