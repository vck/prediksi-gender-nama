import numpy as np

from flask import (
            Flask,
            request, 
            render_template)


clf = SGDClassifier(loss="log")

app = Flask(__name__)


@app.route("/")
def index():
   return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict_gender():
   if request.method=="POST":
      data = predict(request.form['nama'])
      return render_template("index.html", data=data, nama=request.form['nama'])


def predict(name):
   name = tf.transform([name])   

   pred=clf.predict(name)[0]

   prob = clf.predict_proba(name)

   prob_gender = "Laki-laki" if pred == 1 else "Perempuan"
   
   prob_female = round(prob[0][0]*100, 2)
   prob_male = round(prob[0][1]*100, 2)
   return prob_gender, prob_female, prob_male

if __name__ == "__main__":
   app.run()

