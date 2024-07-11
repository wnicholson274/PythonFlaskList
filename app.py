from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request
from calculation import calcBMI
from basicForm import BasicForm

app = Flask(__name__)
bootstrap = Bootstrap5(app)

app.config["SECRET_KEY"] = "Woo"

@app.route('/', methods=["GET", "POST"])
def index():
    form = BasicForm()
    weight = form.weight.data
    height = form.height.data
    if form.validate_on_submit():
        bmi = calcBMI(weight, height)
        return render_template("index.html", form=form, bmi=bmi)
    return render_template("index.html", form=form, bmi=None)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5100 ,debug=True)
