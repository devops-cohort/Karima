from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Colours, Palettes




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

