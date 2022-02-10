from flask import Flask, request, render_template
import pickle
import pandas as pd

app = Flask(__name__)
d=pd.read_csv(r'Animal_Disease_dataset.csv')
model = pickle.load(open("random1.pkl", "rb"))

@app.route("/")

def home():
    AnimalName=sorted(d['AnimalName'].unique())
    symptoms1=sorted(d['symptoms1'].unique())
    symptoms2=sorted(d['symptoms2'].unique())
    symptoms3=sorted(d['symptoms3'].unique())
    symptoms4=sorted(d['symptoms4'].unique())
    symptoms5=sorted(d['symptoms5'].unique())
    AnimalName.insert(0, 'Select animal')
    symptoms1.insert(0, 'Select symptom1')
    symptoms2.insert(0, 'Select symptom2')
    symptoms3.insert(0, 'Select symptom3')
    symptoms4.insert(0, 'Select symptom4')
    symptoms5.insert(0, 'Select symptom5')
    return render_template("Home.html",AnimalName=AnimalName,symptoms1=symptoms1,symptoms2=symptoms2,symptoms3=symptoms3,symptoms4=symptoms4,symptoms5=symptoms5)

@app.route("/predict", methods=["GET", "POST"])

def predict():
    if request.method == "POST":

        # Columns Reading
        AnimalName = request.form.get("AnimalName")
        symptoms1 = request.form.get("symptoms1")
        symptoms2 = request.form.get("symptoms2")
        symptoms3 = request.form.get("symptoms3")
        symptoms4 = request.form.get("symptoms4")
        symptoms5 =request.form.get("symptoms5")

        # prediction = model.predict([[AnimalName,symptoms1,symptoms2,symptoms3,symptoms4,symptoms5]])
        prediction = model.predict(pd.DataFrame([[AnimalName, symptoms1, symptoms2, symptoms3, symptoms4, symptoms5]],
                                                columns=['AnimalName', 'symptoms1', 'symptoms2', 'symptoms3',
                                                         'symptoms4', 'symptoms5']))
        #output = round(prediction[0], 2)

        return render_template('Home.html', prediction_text="Animal Disease is. {}".format(prediction))

    return render_template("Home.html")

if __name__ == "__main__":
    app.run(debug=True)