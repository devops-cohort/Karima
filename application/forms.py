from flask_wtf import FlaskForm
from application import db
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo

from flask_login import LoginManager, current_user

from application.models import Colours, Palettes, Users




#class ColourSearchForm(FlaskForm):

 #   choices = [('Colour','Colour_name')]

  #  select = SelectField('Search for colour: ', choices=choices)
   # search = StringField('')



class PaletteForm(FlaskForm):

    palette_name = StringField('Palette Name',
        validators=[
            DataRequired(),
            Length(min=1, max=150)
        ]
    )

    colour1 = StringField('Colour 1',
        validators=[
            DataRequired(),
            Length(min=1, max=50)
        ]
    )

    colour2 = StringField('Colour 2',
        validators=[
            DataRequired(),
            Length(min=1, max=50)
        ]
    )

    colour3 = StringField('Colour 3',
        validators=[
            DataRequired(),
            Length(min=1, max=50)
        ]
    )

    submit = SubmitField('Make my palette!')

class UpdatePaletteForm(FlaskForm):

    palette_name = StringField('Palette Name',
        validators=[
            DataRequired(),
            Length(min=1, max=150)
        ]
    )

    colour1 = StringField('Colour 1',
        validators=[
            DataRequired(),
            Length(min=1, max=50)
        ]
    )

    colour2 = StringField('Colour 2',
        validators=[
            DataRequired(),
            Length(min=1, max=50)
        ]
    )

    colour3 = StringField('Colour 3',
        validators=[
            DataRequired(),
            Length(min=1, max=50)
        ]
    )

    submit = SubmitField('Update')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    first_name = StringField('First Name',
        validators=[
                DataRequired(),
                Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators=[
                DataRequired(),
                Length(min=2, max=30)
        ]
    )
    submit = SubmitField('Sign Up')
    def validate_email(self, email):

        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email is already in use!')


class LoginForm(FlaskForm):

    email = StringField('Email',
            validators=[
                DataRequired(), 
                Email()
            ]
        )

    password = PasswordField('Password', 
            validators=[
                DataRequired()
            ]
        )

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):

    first_name = StringField('First name', 
            validators=[
                DataRequired(), 
                Length(min=2, max=30)
            ]
        )
    last_name = StringField('Last name', 
            validators=[
                DataRequired(), 
                Length(min=2, max=30)
            ]
        )

    email = StringField('Email', 
            validators=[
                DataRequired(),
                Email()
            ]
        )

    def validate_email(self, email):

        if email.data != current_user.email:

            user = Users.query.filter_by(email=email.data).first()

            if user:
                raise ValidationError('Email already in use')

    submit = SubmitField('Update')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(),Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])

    first_name = StringField('First Name',
        validators=[
                DataRequired(),
                Length(min=2, max=30)
        ]
    )
    last_name = StringField('Last Name',
        validators=[
                DataRequired(),
                Length(min=2, max=30)
        ]
    )
    submit = SubmitField('Sign Up')
    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use!')


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])

    remember = BooleanField('Remember Me')

    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):

    first_name = StringField('First name', validators=[DataRequired(), Length(min=2, max=30)])

    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2, max=30)])

    email = StringField('Email', validators=[DataRequired(),Email()])

    def validate_email(self, email):

        if email.data != current_user.email:

            user = Users.query.filter_by(email=email.data).first()

            if user:

                raise ValidationError('Email already in use')

    submit = SubmitField('Update')

class ColourSearchForm(FlaskForm):
    colours = []
    for colour in Colours.query.all():
       #colours.append(colour.colour_name)
       temp = colour.colour_name, colour.colour_name
       colours.append(temp)
    select = SelectField('Colour Search',choices=colours)
    search = StringField('')
