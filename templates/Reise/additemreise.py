from flask import Flask, redirect, request, flash
from flask.templating import render_template
from flask import Blueprint
import sqlalchemy
from models.models import Reise, Reiseteilnehmer, Reiseveranstalter 

reise_blueprint = Blueprint('blueprint', __name__)

@reise_blueprint.route("/Reisen")
def Reisen():
  
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    Reise = session.query(Reise).order_by(Reise.productCode).all()

    return render_template("reise/reise.html", Reise = Reise)


@reise_blueprint.route("/reise/add", methods=["GET","POST"])
def reise_add():
    session : sqlalchemy.orm.scoping.scoped_session = db.session
    
    add_reise_form = reiseForm()
    
    productlines = session.query(reiseline).order_by(reiseline.productLine).all()
    product_line_list = [(p.productLine, p.productLine) for p in productlines]
    add_reise_form.productLine.choices = product_line_list

    if request.method == 'POST':
        
        if add_product_form.validate_on_submit():
            #hier in db einfügen
            new_product = Product()

            new_product.productCode = add_product_form.productCode.data
            new_product.productName = add_product_form.productName.data
            new_product.productLine = add_product_form.productLine.data
            new_product.productScale = add_product_form.productScale.data
            new_product.productVendor = add_product_form.productVendor.data
            new_product.productDescription = add_product_form.productDescription.data
            new_product.quantityInStock = add_product_form.quantityInStock.data
            new_product.buyPrice = add_product_form.buyPrice.data
            new_product.MSRP = add_product_form.MSRP.data

            db.session.add(new_product)
            db.session.commit()

            return redirect("/reise")
        else:
            return render_template("reise/reiseadd.html",productlines=productlines,form = add_product_form)
    else:
        return render_template("reise/reiseadd.html",productlines=productlines,form = add_product_form)

@products_blueprint.route("/reise/edit", methods=["GET","POST"])
def products_edit():
    session : sqlalchemy.orm.scoping.scoped_session = db.session

    edit_product_form = ProductForm()

    productlines = session.query(Productline).order_by(Productline.productLine).all()
    product_line_list = [(p.productLine, p.productLine) for p in productlines]
    edit_product_form.productLine.choices = product_line_list

    product_code = request.args["productCode"]

    #item laden (wie kann man einen datensatz lesen)
    product_to_edit = session.query(Product).filter(Product.productCode == product_code).first()
    
    if request.method == "POST":
        if edit_product_form.validate_on_submit():
            product_code = edit_product_form.productCode.data
            product_to_edit = db.session.query(Product).filter(Product.productCode == product_code).first()
            
            product_to_edit.productName = edit_product_form.productName.data
            product_to_edit.productLine = edit_product_form.productLine.data
            product_to_edit.productScale = edit_product_form.productScale.data
            product_to_edit.productVendor = edit_product_form.productVendor.data
            product_to_edit.productDescription = edit_product_form.productDescription.data
            product_to_edit.quantityInStock = edit_product_form.quantityInStock.data
            product_to_edit.buyPrice = edit_product_form.buyPrice.data
            product_to_edit.MSRP = edit_product_form.MSRP.data

            db.session.commit()
        return redirect("/reise")
    else:
        edit_product_form.productCode.data = product_to_edit.productCode
        edit_product_form.productName.data = product_to_edit.productName
        edit_product_form.productLine.data = product_to_edit.productLine
        edit_product_form.productScale.data = product_to_edit.productScale
        edit_product_form.productVendor.data = product_to_edit.productVendor
        edit_product_form.productDescription.data = product_to_edit.productDescription
        edit_product_form.quantityInStock.data = product_to_edit.quantityInStock
        edit_product_form.buyPrice.data = product_to_edit.buyPrice
        edit_product_form.MSRP.data = product_to_edit.MSRP

        return render_template("products/products_edit.html",productlines=productlines,form = edit_product_form)

@products_blueprint.route("/products/delete", methods=["post"])
def deleteProduct():
    delete_item_form_obj = ProductDeleteForm()
    if delete_item_form_obj.validate_on_submit():

        product_code_to_delete = delete_item_form_obj.productCode.data
        product_to_delete = db.session.query(Product).filter(Product.productCode == product_code_to_delete)
        product_to_delete.delete()
        
        db.session.commit()
    else:
        print("Fatal Error")
    
    flash(f"Product with id {product_code_to_delete} has been deleted")    