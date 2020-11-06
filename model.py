from sklearn.feature_extraction.text import TfidfVectorizer as tf
from sklearn.model_selection import train_test_split as fuck
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import SGDClassifier
from joblib import dump

def build_model(clf):
   global tf
   tf = tf()
   DATA_PATH = "data/data-2.csv"
    
   X, y = [], []      
   
   with open(DATA_PATH, 'r') as f:
       for line in f:
           X.append(line.split(',')[0].lower())
           y.append(line.split(',')[1].strip('\n'))
  
   y = np.array(y)
   y = np.where(y=='m', 1, 0)
   
   X_train, X_test, y_train, y_test = fuck(X, y, test_size=0.5)
   x_train = tf.fit_transform(X_train)

 
   clf.fit(x_train, y_train)  
   return clf, tf


clf, tf = build_model(clf)


