from application import db

from datetime import datetime

class Colours(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    colour_name = db.Column(db.String(200), nullable=False, unique=True)
    hex_code = db.Column(db.String(100), nullable=False, unique=True)
    hue_cat = db.Column(db.String(200), nullable=False)
    sortment = db.relationship('Sortment', backref= 'coloursort', lazy=True)


    def __repr__(self):
        return ''.join([
            'Colour ID: ', str(self.id), '\r\n',
            'Colour name: ', str(self.colour_name), '\r\n',
            'Hex code: ', str(self.hex_code), '\r\n',
            'Hue category: ', str(self.hue_cat), '\r\n'
        ])

class Palettes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    palette_name = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    sortment = db.relationship('Sortment', backref= 'createsort', lazy=True)
   

    def __repr__(self):
        return ''.join([
            'Palette ID: ', str(self.id), '\r\n',
            'Palette name: ', str(self.palette_name), '\r,\n',
            'Date: ', str(self.date_created), '\r\n'
        ])

class Sortment(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    c_id = db.Column(db.Integer,db.ForeignKey('colours.id') nullable=False)
    p_id = db.Column(db.Integer,db.ForeignKey('palettes.id') nullable=False)
    

    def __repr__(self):
        return ''.join([
            'Sortment ID: ', str(self.id), '\r\n',
            'Colour ID: ', str(self.c_id), '\r\n',
            'Palette ID: ', str(self.p_id), '\r\n'
        ])
