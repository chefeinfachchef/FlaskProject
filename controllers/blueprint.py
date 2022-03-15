from ast import Add
from flask import Flask, request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from Main.additem import AddItemForm
from db.models import Reise, Reiseteilnehmer, Reiseveranstalter
from db.models import db

Reise_blueprint = Blueprint('Reise_blueprint', __name__)

@Reise_blueprint.route("/Reisen")
def Reise():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle products laden
    Reise = session.query(Reise).order_by(Reise.ReiseId).all()

    return render_template("products.html", products = Reise)


@Reise_blueprint.route("/products/add", methods=["GET","POST"])
def products_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    productlines = session.query(Reiseteilnehmer).order_by(Reiseteilnehmer.ReisendeId).all()
    
    addProductForm = AddItemForm()

    if request.method == 'POST':
        
        if addProductForm.validate_on_submit():
            print("gültig")
            return render_template("products_add.html",productlines=productlines, form = addProductForm)
        else:
            raise "Fatal"
    else:
        return render_template("products_add.html",productlines=productlines,form = addProductForm)