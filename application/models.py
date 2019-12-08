from application import db, login_manager

from flask_login import UserMixin

from datetime import datetime

class Colours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colour_name = db.Column(db.String(200), nullable=False, unique=True)
    hex_code = db.Column(db.String(100), nullable=False, unique=True)
    hue_cat = db.Column(db.String(200), nullable=False)

    palettes1 = db.relationship('Palettes', backref = 'palettes1', lazy = True, foreign_keys = 'Palettes.colour1')
    palettes2 = db.relationship('Palettes', backref = 'palettes2', lazy = True, foreign_keys = 'Palettes.colour2')
    palettes3 = db.relationship('Palettes', backref = 'palettes3', lazy = True, foreign_keys = 'Palettes.colour3')


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
    colour1 = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)
    colour2 = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)
    colour3 = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)

    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


   # sortment = db.relationship('Sortment', backref= 'createsort', lazy=True)
    def __repr__(self):
        return ''.join([
            'Palette ID: ', str(self.id), '\r\n',
            'Palette name: ', str(self.palette_name), '\r,\n',
            'Colour 1 ID: ', str(self.colour1), '\r\n',
            'Colour 2 ID: ', str(self.colour2), '\r\n',
            'Colour 3 ID: ', str(self.colour3), '\r\n',
            'Date: ', str(self.date_created), '\r\n'
        ])


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    #Palettes = db.relationship('Palettes', backref='author',lazy=True)
    
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n', 
            'Email: ', self.email, '\r\n', 
            'Name: ',self.first_name, '\r\n', ' ', self.last_name
        ])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

#class Sortment(db.Model):
 #   id = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
  #  c_id = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)
   # p_id = db.Column(db.Integer,db.ForeignKey('palettes.id'), nullable=False)
  # 'def __repr__(self):
   #     return ''.join([
    #        'Sortment ID: ', str(self.id), '\r\n',
     #       'Colour ID: ', str(self.c_id), '\r\n',
      #      'Palette ID: ', str(self.p_id), '\r\n'
       # ])
