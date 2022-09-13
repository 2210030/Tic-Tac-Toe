from enum import unique
from platform import release
from flask import Flask, escape, request, render_template, flash, redirect, url_for, request
import forms
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
# migrate = Migrate(app, db)

class TVShow(db.Model):
    """ This is the table structure which store TV Shows"""
    id = db.Column(db.Integer, primary_key=True)
    no_of_episodes = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(120), nullable=False)
    director = db.Column(db.String(120), nullable=True)
    released_year = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    genre = db.Column(db.String(120), nullable=True)


class Car(db.Model):
    """ This is the table structure which store TV Shows"""
    id = db.Column(db.Integer, primary_key=True)
    seating_capacity = db.Column(db.Integer, nullable=True)
    name = db.Column(db.String(120), nullable=False)
    brand = db.Column(db.String(120), nullable=True)
    type = db.Column(db.String(120), nullable=True)

"""
1. Get all items
This function lists the TV Shows and if there is any 
query parameter then it query the database based on 
the parameter
"""
@app.route('/')
def cars():
    print(request.args.get('q'))
    if request.args.get('q'):
        cars_list = Car.query.filter(Car.name.contains(request.args.get('q')))
    else:
        cars_list = Car.query.all()
    return render_template('cars.html', cars_list=cars_list)




"""
This function shows the details of a single 
item. the detailed view is queried using id 
parameter. 
"""
@app.route('/cars/<id>')
def cars_detail(id):
    print("id", id)
    cars_list = Car.query.filter_by(id=id)
    return render_template('cars_detail.html', cars_list=cars_list)



"""
This function deletes a particular item. 
"""
@app.route('/cars/delete/<id>')
def tvshows_delete(id):
    print("id", id)
    tvs = Car.query.get_or_404(id)
    db.session.delete(tvs)
    db.session.commit()
    flash("Successfully deleted the car", 'success')
    return redirect(url_for('cars'))


"""
This item created a new item.
"""
@app.route('/add-movie', methods=['GET', 'POST'])
def addMovies():
    # db.create_all()
    form = forms.TVShowForm()
    
    if request.method == "POST":
        print(request.form)
        if not request.form.get('name'):
                flash("Name is required", 'danger')
                return render_template('add_movie.html', form=form)

        if request.form.get('released_year'):
            try:
                form.released_year.data = datetime.strptime(request.form['released_year'], "%Y-%m-%d")
            except:
                flash("Invalid released year date", 'danger')
                return render_template('add_movie.html', form=form)

        if request.form.get('end_date'):
            try:
                form.end_date.data = datetime.strptime(request.form['end_date'], "%Y-%m-%d")
            except:
                flash("Invalid end date", 'danger')
                return render_template('add_movie.html', form=form)

        try:
            form.no_of_episodes.data = int(form.no_of_episodes.data)
        except:
            flash("No of episodes should be an integer", 'danger')
            return render_template('add_movie.html', form=form)
        print(form.end_date.data)
        # if form.validate_on_submit():
        name = form.name.data
        director = form.director.data
        no_of_episodes = form.no_of_episodes.data
        released_year = form.released_year.data
        end_date = form.end_date.data
        genre = form.genre.data

        
        data = TVShow(name=name, director=director, no_of_episodes=no_of_episodes,
            released_year=released_year, end_date=end_date, genre=genre)
        db.session.add(data)
        db.session.commit()
        flash("Movie added successfully", 'success')
        return redirect(url_for('tvshows'))
        print(form.name.errors)
    return render_template('add_movie.html', form=form)


"""
This item updates a particular item. 
"""
@app.route('/cars/update/<id>', methods=['GET', 'POST'])
def cars_update(id):
    print("id", id)
    tvs = Car.query.get_or_404(id)
    form = forms.CarForm()
    if request.method == "POST":
        print(request.form)
        if not request.form.get('brand'):
                flash("Brand is required", 'danger')
                return render_template('add_car.html', form=form)

        if not request.form.get('name'):
                flash("Name is required", 'danger')
                return render_template('add_car.html', form=form)

        if not request.form.get('seating_capacity'):
            flash("Seating capacity is required", 'danger')
            return render_template('add_car.html', form=form)

        try:
            form.seating_capacity.data = int(form.seating_capacity.data)
        except:
            flash("Seating Capacity should be an integer", 'danger')
            return render_template('add_car.html', form=form)
        # if form.validate_on_submit():
        # name = form.name.data
        # director = form.director.data
        # no_of_episodes = form.no_of_episodes.data
        # released_year = form.released_year.data
        # end_date = form.end_date.data
        # genre = form.genre.data

        tvs.name = request.form.get('name')
        tvs.brand = request.form.get('brand')
        tvs.type = form.type.data
        tvs.seating_capacity = form.seating_capacity.data
        
        
        # db.session.add(data)
        db.session.commit()
        flash("Car updated successfully", 'success')
        return redirect(url_for('cars'))
        print(form.name.errors)
    else:
        form.name.data = tvs.name
        form.brand.data = tvs.brand
        form.seating_capacity.data = tvs.seating_capacity
        form.type.data = tvs.type
    return render_template('add_car.html', form=form)



###############################################################################
"""
This item created a new item.
"""
@app.route('/add-car', methods=['GET', 'POST'])
def addCar():

    db.create_all()
    form = forms.CarForm()
    
    if request.method == "POST":
        print(request.form)

        if not request.form.get('brand'):
                flash("Brand is required", 'danger')
                return render_template('add_car.html', form=form)

        if not request.form.get('name'):
                flash("Name is required", 'danger')
                return render_template('add_car.html', form=form)

        if not request.form.get('seating_capacity'):
            flash("Seating capacity is required", 'danger')
            return render_template('add_car.html', form=form)

        try:
            form.seating_capacity.data = int(form.seating_capacity.data)
        except:
            flash("Seating Capacity should be an integer", 'danger')
            return render_template('add_car.html', form=form)
        # print(form.end_date.data)
        # if form.validate_on_submit():
        name = form.name.data
        brand = form.brand.data
        seating_capacity = form.seating_capacity.data
        model_released_year = form.model_released_year.data
        type = form.type.data

        
        data = Car(name=name, brand=brand, seating_capacity=seating_capacity,
            type=type)
        db.session.add(data)
        db.session.commit()
        flash("Car added successfully", 'success')
        return redirect(url_for('cars'))
    return render_template('add_car.html', form=form)
