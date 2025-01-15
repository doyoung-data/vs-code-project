from flask import render_template,request,jsonify,Blueprint

view_route = Blueprint('view',__name__)

@view_route.route("/predict")
def predict():
    return render_template("predict.html")