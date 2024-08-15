from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load your model here
# model = pickle.load(open('model.pkl', 'rb'))

def predict_default(loan_amount, income, age, employment_status, credit_score):
    # Example function, replace with your actual model prediction
    # prediction = model.predict([[loan_amount, income, age, employment_status, credit_score]])
    prediction = "Low Risk"  # Mock prediction
    return prediction

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    loan_amount = request.form['loan_amount']
    income = request.form['income']
    age = request.form['age']
    employment_status = request.form['employment_status']
    credit_score = request.form['credit_score']

    prediction = predict_default(loan_amount, income, age, employment_status, credit_score)

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
