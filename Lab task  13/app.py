from flask import Flask, render_template, request
import pickle
import pandas as pd
import os

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "perfume_nn_model_numeric.pkl")
dataset_path = os.path.join(BASE_DIR, "fra_perfumes.csv")  


with open(model_path, "rb") as file:
    data = pickle.load(file)
model = data["model"]
scaler = data.get("scaler")


your_dataset = pd.read_csv(dataset_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        input_data = {
            "Gender": request.form['gender'],
            "Rating Value": float(request.form['rating_value']),
            "Rating Count": int(request.form['rating_count'])
        }

       
        input_data["Gender"] = 0 if input_data["Gender"] == "Male" else 1

        
        input_df = pd.DataFrame([input_data])

       
        input_scaled = scaler.transform(input_df) if scaler else input_df

       
        distances, indices = model.kneighbors(input_scaled, n_neighbors=5)

        recommended = ", ".join([str(your_dataset.iloc[i]["Perfume Name"]) for i in indices[0]])

        return render_template('index.html', prediction_text=f"✨ Recommended Perfume(s): {recommended}")

    except Exception as e:
        return render_template('index.html', prediction_text=f"⚠️ Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
