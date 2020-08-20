from flask import Flask, render_template, request
import numpy as np
import pickle



app = Flask(__name__)


filename = 'diabetes-prediction-rfc-model.pkl'
classifier = pickle.load(open(filename, 'rb'))




@app.route('/')
def Home():
	return render_template('Home.html')

@app.route('/predict', methods=["POST"] )
def predict():
    if request.method == 'POST':
        preg = int(request.form['Pregnancies'])
        glucose = int(request.form['Glucose'])
        bp = int(request.form['BloodPressure'])
        st = int(request.form['Skin Thickness'])
        insulin = int(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        dpf = float(request.form['DiabetesPedigreeFunction'])
        age = int(request.form['Age'])
        data = np.array([[preg, glucose, bp, st, insulin, bmi, dpf, age]])
        
        
        my_prediction = classifier.predict(data)
        
        return render_template('Response.html', prediction=my_prediction)


if __name__ == '__main__':
	app.run()