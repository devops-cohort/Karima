from flask import render_template, redirect, url_for, request
  
from application import app, db, bcrypt

from flask import render_template, redirect, url_for, request, flash
from application.models import Colours, Palettes, Users
from application.forms import UpdatePaletteForm, RegistrationForm, LoginForm, UpdateAccountForm, ColourSearchForm
from flask_login import login_user, current_user, logout_user, login_required

@app.route('/home')
@app.route("/")
def home():
    return render_template('home.html', title='Home')

@app.route('/library', methods=['GET','POST'])
@login_required

def library():
        paletteData = Palettes.query.all()

        return render_template('library.html', title='Library', Palettes=paletteData)

@app.route('/library/delete/<int:id>', methods=['GET','POST'])
@login_required

def delete_palette(id):

    palette_delete = Palettes.query.filter_by(id=id).first()

    db.session.delete(palette_delete)
    db.session.commit()

    return redirect(url_for('library'))



@app.route('/update', methods=['GET','POST'])
@login_required

def update():

    form = ColourSearchForm()
    colour_search = ColourSearchForm(request.form)

    if request.method == 'POST':
        palettes = Palettes(colour1=form.select1.data, colour2=form.select2.data, colour3=form.select3.data, user_id=current_user.get_id())
        #print(form.select1.data)
        #print(form.select2.data)
        #print(form.select3.data)


        db.session.add(palettes)
        db.session.commit()

        return redirect(url_for('library'))

    else:
        print(form.errors)
    return render_template('create.html', title='Palette', form=form)

#    palette= Palettes.query.filter_by(id=form.paletteid.data)()

 #   form = ColourSearchForm()
  #  colour_search = ColourSearchForm(request.form)

   # if request.method == 'POST':
    #    search = colour_search.data['select']

     #   db.session.add(Palettes)
      #  db.session.commit()

       # return render_template('library.html',form=colour_search)

  #  else:
   #     print(form.errors)
   # return render_template('update.html', title='Palette', form=form)



@app.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    if form.validate_on_submit():

        user=Users.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):

            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')

            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))

    return render_template('login.html', title = 'Login',form=form)




@app.route('/register', methods=['GET','POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('home'))

    form = RegistrationForm()

    if form.validate_on_submit():

        hashed_pw = bcrypt.generate_password_hash(form.password.data)

        user = Users(
            first_name=form.first_name.data,
            last_name=form.first_name.data,
            email=form.email.data,
            password=hashed_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))
    return render_template('register.html', title = 'Register', form=form)


@app.route('/create', methods=['GET','POST'])
@login_required

def create():
    form = ColourSearchForm()
    colour_search = ColourSearchForm(request.form)

    if request.method == 'POST':
        palettes = Palettes(colour1=form.select1.data, colour2=form.select2.data, colour3=form.select3.data, user_id=current_user.get_id())
        #print(form.select1.data)
        #print(form.select2.data)
        #print(form.select3.data)


        db.session.add(palettes)
        db.session.commit()

        return redirect(url_for('library'))

    else:
        print(form.errors)
    return render_template('create.html', title='Palette', form=form)


#def create():

    #form = PaletteForm()
   # if form.validate_on_submit():

        #colour1_id = Colours.query.filter_by(colour_name=form.colour1.data).first().id
        #colour2_id = Colours.query.filter_by(colour_name=form.colour2.data).first().id
       # colour3_id = Colours.query.filter_by(colour_name=form.colour3.data).first().id

       # palettedata = Palettes(
            #palette_name = form.palette_name.data,
            #colour1 = colour1.data,
            #colour2 = colour2.data,
            #colour3 = colour3.data
        #)

        #colour_id = Colours.query.filter_by(colour_name=form.colour_name.data).all()

        #db.session.add(palettedata)
        #db.session.commit()

        #return redirect(url_for('library'))

    #else:
     #   print(form.errors)
   # return render_template('create.html', title='Palette', form=form)


@app.route("/logout")
def logout():

    logout_user()

    return redirect(url_for('login'))

@app.route('/account', methods=['GET','POST'])
@login_required

def account():

    form = UpdateAccountForm()

    if form.validate_on_submit():

        current_user.first_name = form.first_name.data
        current_user.last_name = form.last_name.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('account'))

    elif request.method == 'GET':
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        form.email.data = current_user.email

    return render_template('account.html', title='Account', form=form)

