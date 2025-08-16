# 🩺 AI-Based Disease Prediction System (Heart, Diabetes & Parkinson)

This project is a machine learning-based predictive system that analyzes patient data to detect the likelihood of three major health conditions: **Heart Disease**, **Diabetes**, and **Parkinson's Disease**. It uses **Logistic Regression** models to perform classification based on medical parameters.

---

## 🔍 Features

- 🫀 Predicts **Heart Disease** based on medical attributes (age, cholesterol, blood pressure, etc.)
- 🩸 Detects **Diabetes** using common diagnostic indicators like glucose level, BMI, insulin, etc.
- 🧠 Classifies **Parkinson’s Disease** based on voice-related biomedical features
- 🔎 Simple predictive system using Logistic Regression for fast and interpretable results
- 📈 Model evaluation using accuracy score, confusion matrix, and more

---

## ⚙️ Tech Stack

- **Python 3.8+**
- **Pandas** – Data processing
- **NumPy** – Numerical operations
- **Scikit-learn** – ML modeling, training, evaluation
- **Jupyter Notebook / Google Colab** – Development environment

---

## 📁 Project Structure

├── heart_disease_model.ipynb
├── diabetes_model.ipynb
├── parkinson_model.ipynb
├── /datasets
│ ├── heart_disease_data.csv
│ ├── diabetes.csv
│ ├── parkinsons.csv
└── README.md

yaml
Copy
Edit

---

## 🧪 How It Works

1. **Data Collection**  
   Reads structured datasets for each disease from CSV files.

2. **Preprocessing**  
   - Splits features and target labels  
   - Handles missing values and categorical data if present  
   - Scales or normalizes features where necessary

3. **Model Training**  
   Uses Logistic Regression to train models for each disease.

4. **Evaluation**  
   Prints accuracy on training and test data using `accuracy_score`.

5. **Prediction System**  
   Accepts patient input data and predicts whether the person is at risk.

---

## ✅ Sample Prediction Logic

```python
# Input sample for heart disease
input_data = (67,1,0,120,229,0,0,129,1,2.6,1,2,3)

# Convert to NumPy array and reshape
input_data_reshaped = np.asarray(input_data).reshape(1, -1)

# Predict using trained model
prediction = model.predict(input_data_reshaped)

if prediction[0] == 0:
    print("The Person does not have Heart Disease")
else:
    print("The Person has Heart Disease")
(Similar logic applies for Diabetes and Parkinson models)

🧬 Datasets Used
Heart Disease Dataset – UCI Repository / Kaggle

Diabetes Dataset – Pima Indians Diabetes Database

Parkinson’s Dataset – UCI Machine Learning Repository

🚀 Getting Started
📥 Installation
bash
Copy
Edit
pip install pandas numpy scikit-learn
🏃‍♂️ Run the Model
Use Jupyter Notebook or Google Colab to open:

heart_disease_model.ipynb

diabetes_model.ipynb

parkinson_model.ipynb

📊 Performance Metrics
Each model is evaluated using:

Accuracy Score

Confusion Matrix

Precision, Recall, F1-score (optional)

📌 Author
Shubh Shah
AI & Data Science | Python | ML | Data Analytics
LinkedIn | GitHub

📃 License
This project is open-source and available under the MIT License.

yaml
Copy
Edit

---

Let me know if you also want a **`requirements.txt`** or separate `README.md` for each disease model.







