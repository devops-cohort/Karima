from flask_wtf import FlaskForm
from application import db
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError, Email, EqualTo

from flask_login import LoginManager, current_user

from application.models import Colours, Palettes, Users



class ColourSearchForm(FlaskForm):
    colours = []
    query = Colours.query.all()
    for colour in query:
       #colours.append(colour.colour_name)
       temp = colour.colour_name, colour.colour_name
       colours.append(temp)
    select1 = SelectField('Colour pick',choices=colours)
    select2 = SelectField('Colour pick',choices=colours)
    select3 = SelectField('Colour pick',choices=colours)

    submit = SubmitField ('Make my palette!')


class UpdatePaletteForm(FlaskForm):

    colours = []
    query = Colours.query.all()
    for colour in query:
       #colours.append(colour.colour_name)
       temp = colour.colour_name, colour.colour_name
       colours.append(temp)
    select1 = SelectField('Colour pick',choices=colours)
    select2 = SelectField('Colour pick',choices=colours)
    select3 = SelectField('Colour pick',choices=colours)

    submit = SubmitField ('Update my palette!')

   # colours = []
  #  for colour in Colours.query.all():

     #  temp = colour.colour_name, colour.colour_name
    #   colours.append(temp)
   # select = SelectField('Colour Search',choices=colours)
  #  search = StringField('')

 #   submit = SubmitField('Update')

#class DeletePaletteForm(FlaskForm):

 #   palette = StringField('Palette ID: ',
  #          validators=[
   #             DataRequired(),
#                Length(min=2, max=30)
 #       ]
  #  )
    
   # submit = SubmitField('Delete palette')

    #def validate_palette_id(self, id):
     #   exist = Palettes.query.filter_by(p_id = id).first()
      #  if exist == False:
       #     raise ValidationError('Palette not found')



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

    first_name = StringField('First name', validators=[DataRequired(), Length(min=2, max=30)])

    last_name = StringField('Last name', validators=[DataRequired(), Length(min=2, max=30)])

    email = StringField('Email', validators=[DataRequired(),Email()])

    def validate_email(self, email):

        if email.data != current_user.email:

            user = Users.query.filter_by(email=email.data).first()

            if user:

                raise ValidationError('Email already in use')

    submit = SubmitField('Update')

