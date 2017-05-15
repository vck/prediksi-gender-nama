from sklearn.feature_extraction.text import CountVectorizer as fuckkk
from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.model_selection import train_test_split as fuck
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier

import numpy as np

from flask import (
            Flask,
            request, 
            render_template)


clf = SGDClassifier(loss="log")

app = Flask(__name__)


def save_model(clf, name):
   with open(name, 'wb') as f:
      pickle.dump(clf, f   )
      print("model saved!")


def build_model(clf):
   global tf
   tf = tf()
   DATA_PATH = "data/data-2.csv"
    
   X, y = [], []      
   
   with open(DATA_PATH, 'r') as f:
       for line in f:
           X.append(line.split(',')[0].lower())
           y.append(line.split(',')[1].strip('\n'))
  
   # new label, turn m&f into 1 and 0
   y = np.array(y)
   y = np.where(y=='m', 1, 0)
   
   X_train, X_test, y_train, y_test = fuck(X, y, test_size=0.5)
   x_train = tf.fit_transform(X_train)

 
   clf.fit(x_train, y_train)  
   #print(clf.score(x_train, y_train))   
   return clf, tf


clf, tf = build_model(clf)

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

