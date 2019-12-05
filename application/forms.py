from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Colours
    ###import all tables or?


class PaletteForm(FlaskForm):

    name = StringField('Palette Name',
        validators=[
            DataRequired(),
            Length(min=1, max=100)
        ]
    )

    colour1 = StringField('Colour 1',
        validators=[
            DataRequired(),
            Length(min=2, max=20)
        ]
    )

    colour2 = StringField('Colour 2',
        validators=[
            DataRequired(),
            Length(min=2, max=200)
        ]
    )

    colour3 = StringField('Colour 3',
        validators=[
            DataRequired(),
            Length(min=2, max=20)
        ]
    )

    submit = SubmitField('Make my palette!')


class RandomForm(Flaskform):

    ###how to random???

    submit = SubmitField('Surprise me!')
