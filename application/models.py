from application import db, login_manager

from flask_login import UserMixin

from datetime import datetime

#sortment = db.Table('', db.Model.metadata,
#    db.Column('c_id', db.Integer, db.ForeignKey('colours.id'), nullable=False),
#    db.Column('p_id', db.Integer, db.ForeignKey('palettes.id'), nullable=False)
#    )

class Colours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    colour_name = db.Column(db.String(200), nullable=False, unique=True)
    hex_code = db.Column(db.String(100), nullable=False, unique=True)
    hue_cat = db.Column(db.String(200), nullable=False)

        #palettes = db.relationship('Palettes', secondary = sortment, backref = db.backref('sortment', lazy = 'dynamic'))
   # palettes1 = db.relationship('Palettes', backref = 'palettes1', foreign_keys = 'Palettes.colour1', lazy = 'dynamic')
   # palettes2 = db.relationship('Palettes', backref = 'palettes2', foreign_keys = 'Palettes.colour2', lazy = 'dynamic')
   # palettes3 = db.relationship('Palettes', backref = 'palettes3', foreign_keys = 'Palettes.oolour3', lazy = 'dynamic')


    def __repr__(self):
        return ''.join([
            'Colour ID: ', str(self.id), '\r\n',
            'Colour name: ', str(self.colour_name), '\r\n',
            'Hex code: ', str(self.hex_code), '\r\n',
            'Hue category: ', str(self.hue_cat), '\r\n'
        ])

class Palettes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #colour1 = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)
   # colour2 = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)
   # colour3 = db.Column(db.Integer,db.ForeignKey('colours.id'), nullable=False)
    colour1 = db.Column(db.String(100), nullable=False)
    colour2 = db.Column(db.String(100), nullable=False)
    colour3 = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


    def __repr__(self):
        return ''.join([
            'Palette ID: ', str(self.id), '\r\n',
            'Colour 1 ID: ', str(self.colour1), '\r\n',
            'Colour 2 ID: ', str(self.colour2), '\r\n',
            'Colour 3 ID: ', str(self.colour3), '\r\n',
            'User ID: ', str(self.user_id), '\r\n',
            'Date: ', str(self.date_created), '\r\n'
        ])



class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(500), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    palettes = db.relationship('Palettes', backref='author',lazy=True)

   #palettes = db.relationship('Palettes', backref='creator', lazy='dynamic',  primaryjoin="User.id == Palettes.user.id")


    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.id), '\r\n',
            'Email: ', self.email, '\r\n',
            'Name: ',self.first_name, '\r\n', ' ', self.last_name
        ])

@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))

