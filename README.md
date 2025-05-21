# 💼 Insurance Cost Prediction App

This is a **Streamlit web application** that predicts the **medical insurance cost** of a person based on features like age, gender, BMI, smoking status, region, and number of children. It uses machine learning models (XGBoost, Decision Tree, and Linear Regression) trained on real-world insurance data.

---

## 🚀 Features

- Predicts insurance charges based on user input
- Preprocessing includes OneHotEncoding for categorical features
- Compares multiple ML models and evaluates performance
- Deployable with Streamlit for real-time prediction

---

## 🧠 Technologies Used

- Python
- Streamlit
- Pandas, NumPy
- Scikit-learn
- XGBoost
- Joblib
- Git

---

## 📦 Dataset

Used: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)

---

## 🏁 How to Run Locally

### 1. Clone the repository

git clone (https://github.com/shirnamvijay/MICP.git)
cd your-repo-name

### 2. Install dependencies
pip install -r requirements.txt

### 3. Run the Streamlit app
streamlit run app.py

---

## ✍️ Input Fields

| Field      | Type     | Description                       |
|------------|----------|-----------------------------------|
| Age        | Integer  | Age of the person (e.g., 28)      |
| Sex        | String   | male / female                     |
| BMI        | Float    | Body Mass Index (e.g., 26.2)      |
| Children   | Integer  | Number of children                |
| Smoker     | String   | yes / no                          |
| Region     | String   | northeast, northwest, southeast, southwest |

---

## 📈 Model Performance

| Model             | MAE    | RMSE   |
|-------------------|--------|--------|
| Linear Regression | 4181.1 | 5796.2 |
| Decision Tree     | 3195.1 | 6515.1 |
| XGBoost           | 2567.3 | 4595.6 |

(Replace with your actual evaluation results.)

---

## 📁 File Structure

├── app.py # Streamlit app
├── insurance_model.pkl # Saved ML model
├── insurance.csv # Dataset
├── requirements.txt # Dependencies
└── README.md # You're here!

---

## 🙌 Credits

- Developed by [Vijay Shirnam]
- Dataset from [Kaggle](https://www.kaggle.com/datasets/mirichoi0218/insurance)

---

## 📤 Deployment (Optional)

You can deploy this app for free using [Streamlit Cloud](https://streamlit.io/cloud).
