from flask import render_template, redirect, url_for, request
  
from application import app, db

from application.models import Colours, Palettes, Sortment
from application.forms import PaletteForm, UpdatePaletteForm


@app.route('/home')
@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PaletteForm()
    if form.validate_on_submit():
        palettedata = Palettes(
            palette_name=form.palette_name.data,
            colour1=form.colour1.data,  
            colour2=form.colour2.data,
            colour3=form.colour3.data
        )

        db.session.add(palettedata)
        db.session.commit()
        return redirect(url_for('library'))
    else:
        print(form.errors)

    return render_template('create.html', title='Create a palette', form=form)


@app.route('/library', methods=['GET','POST'])
def library():
    return render_template('library.html', title='Library')



@app.route('/update', methods=['GET','POST'])
def update():
    form = UpdatePaletteForm()
    palette= Palettes.query.filter_by(id=form.id.data)()
    

    if form.validate_on_submit():
        Palettes.palette_name = form.palette_name.data
        Palettes.colour1 = form.colour1.data
        Palettes.colour2 = form.colour2.data
        Palettes.colour3 = form.colour3.data
        db.session.commit()
        return redirect(url_for('library'))
    elif request.method == 'GET':
        form.palette_name.data = Palettes.palette_name
        form.colour1.data = Palettes.colour1
        form.colour2.data = Palettes.colour2
        form.colour3.data = Palettes.colour3

    return render_template('update.html', title='Update', form=form)

