# from flask_wtf import FlaskForm
# from wtforms import StringField, PasswordField, SubmitField
# from wtforms.validators import DataRequired, Email, EqualTo


# class UpdateProfileForm(FlaskForm):
#     username = StringField('Username', validators=[DataRequired()])
#     email = StringField('Email', validators=[DataRequired(), Email()])
#     password = PasswordField('Current Password', validators=[DataRequired()])
#     new_password = PasswordField('New Password', validators=[EqualTo('confirm_password', message='Passwords must match')])
#     confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
#     submit = SubmitField('Update Profile')
