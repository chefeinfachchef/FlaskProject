from ast import Add
from flask import Flask, redirect, request
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models.models import Reise, Reiseteilnehmer, Reiseveranstalter
from models.models import db

Reise_blueprint = Blueprint('Reise_blueprint', __name__)

@Reise_blueprint.route("/Reisen")
def Reise():
    #workaround für sesssion Autocomplete
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    #alle products laden
    Reise = session.query(Reise).order_by(Reise.ReiseId).all()

    return render_template("products.html", Reise = Reise)


@Reise_blueprint.route("/products/add", methods=["GET","POST"])
def products_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    productlines = session.query(Reise).order_by(Reise).all()
    
    addProductForm = Reiseveranstalter()

    if request.method == 'POST':
        
        if addProductForm.validate_on_submit():
            #hier in db einfügen
            newReise = Reise()

            newReise.productCode = addProductForm.productCode.data
            newReise.productName = addProductForm.productName.data
            newReise.productLine = addProductForm.productLine.data
            newReise.productScale = addProductForm.productScale.data
            newReise.productVendor = addProductForm.productVendor.data
            newReise.productDescription = addProductForm.productDescription.data
            newReise.quantityInStock = addProductForm.quantityInStock.data
            newReise.buyPrice = addProductForm.buyPrice.data
            newReise.MSRP = addProductForm.MSRP.data

            db.session.add(newReise)
            db.session.commit()

            return redirect("/products")
        else:
            return render_template("products_add.html",productlines=productlines,form = addProductForm)
    else:
        return render_template("products_add.html",productlines=productlines,form = addProductForm)