# ANN Customer Churn Classification

An Artificial Neural Network (ANN) powered Machine Learning Web App to predict Customer Churn based on customer behavior and demographics.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Try%20it%20Here!-blue)](https://ann-customer-churn-classification-fsc5cdqgtkq3emcxnhxnhv.streamlit.app/)

<p align="center">
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" alt="TensorFlow"/>
  <img src="https://img.shields.io/badge/Keras-D00000?style=for-the-badge&logo=keras&logoColor=white" alt="Keras"/>
  <img src="https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
</p>

## 🚀 Project Overview

Customer churn prediction helps companies identify customers who are likely to leave (churn) and take proactive retention actions. This model analyzes multiple customer features to predict the *probability of churn* using a trained Artificial Neural Network.

### Features Used for Prediction:
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

## 📊 Tech Stack

| Tool/Library | Purpose |
|--------------|---------|
| TensorFlow / Keras | Building & Training the ANN Model |
| Scikit-Learn | Preprocessing (Scaling, Encoding) |
| Streamlit | Frontend Web App |
| Pickle | Saving Encoders & Scaler |

## 🖥️ App Features

- Clean User Interface with Streamlit
- User-friendly Inputs
- Live ANN Model Prediction
- Churn Probability Output
- Clear Classification Output (Churn / No Churn)

## 🗂️ Repository Structure

```
├── app.py                    # Main Streamlit App 
├── model.h5                  # Trained ANN Model 
├── label_encoder_gender.pkl  # Gender Encoder
├── onehot_encoder_geo.pkl    # Geography Encoder
├── scaler.pkl                # Scaler for Feature Scaling 
├── experiments.ipynb         # EDA, Model Training Notebook 
├── prediction.ipynb          # Prediction Testing Notebook 
├── requirements.txt          # Project Dependencies
└── runtime.txt               # Python version for Streamlit Cloud
```

## ⚙️ Installation for Local Testing

```bash
# Clone the repository
git clone https://github.com/MuaazSM/ANN-Customer-Churn-Classification.git

# Navigate to project directory
cd ANN-Customer-Churn-Classification

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

## 🖥 Live Deployment

Deployed on Streamlit Cloud:
→ [https://ann-customer-churn-classification-fsc5cdqgtkq3emcxnhxnhv.streamlit.app/](https://ann-customer-churn-classification-fsc5cdqgtkq3emcxnhxnhv.streamlit.app/)

## ✨ Future Improvements

- [ ] Add Model Performance Metrics
- [ ] Add Data Visualizations for Insights
- [ ] Add Feature Importance Analysis
- [ ] Deploy on AWS / Azure / GCP
- [ ] User Authentication

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the GNU General Public License - see the [LICENSE](LICENSE) file for details.

## 🙌 Credits

Made with ❤️ by Muaaz Shaikh
