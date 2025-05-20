from flask import Flask, render_template, request
import joblib

# Load the trained model
model = joblib.load('saved_model.pkl')

app = Flask(__name__)

# Function to encode categorical data to numeric values
def encode_input(data):
    categorical_columns = ['rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane']
    for i, feature in enumerate(data):
        if feature in ['normal', 'abnormal', 'yes', 'no', 'good', 'poor', 'present', 'not_present']:
            if feature == 'normal': data[i] = 0
            elif feature == 'abnormal': data[i] = 1
            elif feature == 'yes': data[i] = 1
            elif feature == 'no': data[i] = 0
            elif feature == 'good': data[i] = 0
            elif feature == 'poor': data[i] = 1
            elif feature == 'present': data[i] = 1
            elif feature == 'not_present': data[i] = 0
    return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the input from the form
        data = [
            float(request.form['age']),
            float(request.form['bp']),
            float(request.form['sg']),
            float(request.form['al']),
            float(request.form['su']),
            request.form['rbc'],
            request.form['pc'],
            request.form['pcc'],
            request.form['ba'],
            float(request.form['bgr']),
            float(request.form['bu']),
            float(request.form['sc']),
            float(request.form['sod']),
            float(request.form['pot']),
            float(request.form['hemo']),
            float(request.form['pcv']),
            float(request.form['wc']),
            float(request.form['rc']),
            request.form['htn'],
            request.form['dm'],
            request.form['cad'],
            request.form['appet'],
            request.form['pe'],
            request.form['ane']
        ]
        
        # Encode categorical data
        encoded_data = encode_input(data)
        
        # Make the prediction
        prediction = model.predict([encoded_data])[0]
        
        # Output result
        prediction_text = "The patient has Chronic Kidney Disease" if prediction == 1 else "The patient does not have Chronic Kidney Disease"
        
        # Pass both prediction and original input data to the result page
        return render_template('result.html', prediction_text=prediction_text, submitted_data=request.form)
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

