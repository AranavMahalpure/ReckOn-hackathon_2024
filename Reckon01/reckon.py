from flask import Flask,render_template,url_for
app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/form",methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        url = request.form['url']
    return render_template("form.html")

app.run(debug=True)
# from flask import Flask, jsonify

# app = Flask(__name__)
# from joblib import load

# mainmodel = load('models/energy-model.pkl')
# scalemodel = load('models/energy-scaler.pkl')
# @app.route('/')
# def predict():
#     volt = 240
#     Sub_1 = 240
#     Sub_2 = 240
#     Sub_3 = 240
#     sd = scalemodel.transform([[0, volt, 241.2317, Sub_1, Sub_2, Sub_3]])
#     p1 = mainmodel.predict([[sd[0, 1], sd[0, 3], sd[0, 4], sd[0, 5]]])
#     sd[0, 0] = p1
#     ans = scalemodel.inverse_transform(sd)
#     return jsonify({'prediction': ans[0, 0]})

# if __name__ == '__main__':
#     app.run(debug=True)