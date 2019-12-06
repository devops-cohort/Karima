from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

from application.models import Colours, Palettes, Sortment


class PaletteForm(FlaskForm):

    palette_name = StringField('Palette Name',
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


class UpdatePaletteForm(FlaskForm):

    palette_name = StringField('Palette Name',
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

    submit = SubmitField('Update')

###class DeletePaletteForm(FlaskForm):



###class RandomForm(FlaskForm):

    ###how to random??

   ## #submit = SubmitField('Surprise me!')
