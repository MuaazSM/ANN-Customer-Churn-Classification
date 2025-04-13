# ANN Customer Churn Classification

An Artificial Neural Network (ANN) powered Machine Learning Web App to predict Customer Churn based on customer behavior and demographics.

Built using:
- TensorFlow / Keras
- Scikit-Learn
- Streamlit
- Python

→ Live Demo: [Try it Here!](https://ann-customer-churn-classification-fsc5cdqgtkq3emcxnhxnhv.streamlit.app/)

---

## 🚀 Project Overview
Customer churn prediction helps companies identify customers who are likely to leave (churn) and take action proactively.

This model uses:
- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

to predict the *probability of churn* using an ANN trained model.

---

## 📊 Tech Stack
| Tool/Library | Purpose |
|--------------|---------|
|TensorFlow / Keras|Building & Training the ANN Model|
|Scikit-Learn|Preprocessing (Scaling, Encoding)|
|Streamlit|Frontend Web App|
|Pickle|Saving Encoders & Scaler|

---

## 🖥️ App Features
- Clean User Interface with Streamlit
- User-friendly Inputs
- Live ANN Model Prediction
- Churn Probability Output
- Clear Classification Output (Churn / No Churn)

---

## 🗂️ Repository Structure
├── app.py # Main Streamlit App 
├── model.h5 # Trained ANN Model 
├── label_encoder_gender.pkl 
├── onehot_encoder_geo.pkl 
├── scaler.pkl # Scaler for Feature Scaling 
├── experiments.ipynb # EDA, Model Training Notebook 
├── prediction.ipynb # Prediction Testing Notebook 
├── requirements.txt 
└── runtime.txt # Python version for Streamlit Cloud


---

## ⚙️ Installation for Local Testing

```bash
git clone https://github.com/MuaazSM/ANN-Customer-Churn-Classification.git
cd ANN-Customer-Churn-Classification
pip install -r requirements.txt
streamlit run app.py
🖥 Live Deployment
Deployed on Streamlit Cloud:
→ https://ann-customer-churn-classification-fsc5cdqgtkq3emcxnhxnhv.streamlit.app/

✨ Future Improvements
Add Model Performance Metrics

Add Data Visualizations for Insights

Add Feature Importance

Deploy on AWS / Azure / GCP

User Authentication

🙌 Credits
Made with ❤️ by Muaaz Shaikh
