from application import db
from application.models import Colours, Palettes

db.create_all()

red = "red"
yellow = "yellow"
blue = "blue"

#colours1 = Colours( colour_name = form., hex_code="#456789", hue_cat="red" )
#colours2 = Colours( colour_name = yellow, hex_code="#789456", hue_cat="blue" )
#colours3 = Colours( colour_name = blue, hex_code="#123456", hue_cat="yellow" )

#db.session.add(colours1)
#db.session.add(colours2)
#db.session.add(colours3)

colour_id = Colours.query.filter_by(colour_name=form.colour_name.data).first().id

palletes = Palettes(palette_name=form.palette_name.data, colour1=colour1_id, colour2=colour2_id, colour3=colour3_id)

db.session.add(palletes)


db.session.commit()
