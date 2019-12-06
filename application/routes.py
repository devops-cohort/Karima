from flask import render_template, redirect, url_for, request
  
from application import app, db

from flask import render_template, redirect, url_for, request, flash
from application.models import Colours, Palettes
from application.forms import PaletteForm, UpdatePaletteForm


@app.route('/home')
@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PaletteForm()
    if form.validate_on_submit():
        colour1_id = Colours.query.filter_by(colour_name=form.colour1.data).first().id
        colour2_id = Colours.query.filter_by(colour_name=form.colour2.data).first().id
        colour3_id = Colours.query.filter_by(colour_name=form.colour3.data).first().id

        palettedata = Palettes(
            palette_name = form.palette_name.data,
            colour1 = colour1.data,  
            colour2 = colour2.data,
            colour3 = colour3.data
        )

            colour_id = Colours.query.filter_by(colour_name=form.colour_name.data).first().id

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
    palette= Palettes.query.filter_by(palette_name=form.palette_name.data)()
    

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


#@app.route('/create', methods=['GET', 'POST']) ### '/' page for where it'll be or?
#def colourindex():
   # search = ColourSearchForm(request.form)
  #  if request.method == 'POST':
   #     return search_results(search)

 #   return render_template('index.html', form=search)

#@app.route('/results')
#def search_results(search):
    #results = []
    #search_string = search.data['search']

   # if search.data['search'] == '':
       # query = db_session.query()  #### << what in ()?
  #      results = query.all()

 #   if not results:
        #flash('No results found!')
       # return redirect('/')
   # else:
        ## display results
        #return render_template('results.html', results=results)
