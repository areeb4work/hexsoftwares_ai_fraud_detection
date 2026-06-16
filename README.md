# 🔍 AA — AI Fraud Detection System

> Real-time credit card fraud detection powered by Machine Learning, built with a clean and interactive Streamlit web interface.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

## 📌 Overview

The **AA Fraud Detection System** is an end-to-end machine learning application that analyzes credit card transactions in real time and classifies them as **Legitimate**, **Suspicious**, or **Fraudulent**. Trained on a real-world Kaggle dataset of 284,807 transactions, the model achieves **99.9% accuracy** and is deployed through an elegant, interactive web interface.

This project demonstrates the full ML pipeline — from raw data and feature engineering all the way to a production-ready web application.

---

## ✨ Features

- 🚨 **Real-Time Fraud Detection** — Instantly analyzes any transaction and returns a fraud probability score
- 📊 **Three-Tier Classification** — Transactions are classified as `LEGITIMATE ✅`, `SUSPICIOUS ⚠️`, or `FRAUD 🚨`
- 💡 **Actionable Recommendations** — System recommends to Approve, Flag for Review, or Block the transaction
- 🎛️ **28 Interactive PCA Feature Sliders** — Full control over all V1–V28 anonymized PCA features
- 💰 **Adjustable Transaction Inputs** — Customizable transaction amount and time inputs
- 📈 **Live Metrics Dashboard** — Displays fraud probability, prediction status, and transaction amount post-analysis
- 🎨 **Custom Dark Purple UI** — Elegant gradient-themed interface with animated result cards

---

## 🧠 How It Works

The model was trained on the [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud), which contains anonymized features derived from PCA transformation to protect cardholder privacy.

**Prediction Pipeline:**

```
User Input (Amount + Time + V1–V28)
        ↓
Feature Scaling (StandardScaler normalization)
        ↓
ML Model Inference (fraud_detection_model.pkl)
        ↓
Probability Score + Classification
        ↓
Visual Result + Recommended Action
```

**Classification Thresholds:**
| Result | Condition |
|---|---|
| ✅ LEGITIMATE | Predicted class = 0 AND probability < 30% |
| ⚠️ SUSPICIOUS | Predicted class = 0 BUT probability ≥ 30% |
| 🚨 FRAUD | Predicted class = 1 |

---

## 🗂️ Dataset

| Property | Details |
|---|---|
| **Source** | [Kaggle — Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |
| **Total Transactions** | 284,807 |
| **Fraudulent Cases** | 492 (~0.17% — highly imbalanced) |
| **Features** | 30 (V1–V28 PCA components + `Amount` + `Time`) |
| **Target Variable** | `Class` (0 = Legitimate, 1 = Fraud) |

> ⚠️ The dataset is highly imbalanced. Handling this imbalance was a key challenge in achieving reliable model performance.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Language** | Python 3.8+ |
| **Machine Learning** | Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Model Serialization** | Joblib |
| **Web Framework** | Streamlit |
| **Notebook** | Jupyter Notebook |
| **Dataset** | Kaggle Credit Card Fraud Detection |

---

## 📁 Project Structure

```
AA-Fraud-Detection/
│
├── app.py                        # Streamlit web application
├── AI_Fraud_Detection.ipynb      # Model training & evaluation notebook
├── fraud_detection_model.pkl     # Serialized trained ML model
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/AA-Fraud-Detection.git
cd AA-Fraud-Detection
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the application**
```bash
streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📦 Dependencies

```txt
streamlit
scikit-learn
pandas
numpy
joblib
```

Install all at once:
```bash
pip install streamlit scikit-learn pandas numpy joblib
```

---

## 🖥️ App Interface

| Section | Description |
|---|---|
| **Hero Banner** | AA branding with project title and author |
| **Stats Row** | Dataset size, model accuracy, detection speed, tech used |
| **Transaction Details** | Amount, time, and all 28 PCA feature inputs |
| **Detection Result** | Animated card showing fraud status and probability |
| **Result Metrics** | Fraud probability %, prediction label, transaction amount |

---

## 📊 Model Performance

| Metric | Value |
|---|---|
| **Accuracy** | 99.9% |
| **Dataset Size** | 284,807 transactions |
| **Training Approach** | Supervised Classification |
| **Input Features** | 30 (scaled amount + scaled time + V1–V28) |

> The model uses scaled versions of `Amount` and `Time` features (mean normalization applied during preprocessing).

---

## 🔬 Notebook

The `AI_Fraud_Detection.ipynb` Jupyter notebook covers the full ML workflow:

- Exploratory Data Analysis (EDA)
- Class imbalance analysis
- Feature scaling and preprocessing
- Model training and selection
- Evaluation (accuracy, precision, recall, confusion matrix)
- Model export with Joblib

---

## ⚙️ Feature Scaling (Applied in App)

```python
scaled_amount = (amount - 88.35)  / 250.12
scaled_time   = (time   - 94813)  / 47488
```

These constants are derived from the training dataset distribution to normalize inputs consistently with what the model was trained on.

---

## ⚠️ Disclaimer

This project is developed **strictly for educational and portfolio purposes**. It is not intended for use in production financial systems or real-world fraud prevention pipelines without further validation, compliance review, and security auditing.

- The dataset used is publicly available on Kaggle and all features are anonymized via PCA.
- The model's predictions should **not** be used to make real financial decisions.
- The author assumes **no liability** for any decisions made based on this tool.

---

## 👤 Author

**Areeb Ahsan**

> Built with passion for AI, FinTech, and real-world problem solving.

- 🔗 [LinkedIn](https://linkedin.com/in/your-profile)
- 💻 [GitHub](https://github.com/your-username)

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with attribution.

---

## 🙌 Acknowledgements

- [Kaggle](https://www.kaggle.com/) for the Credit Card Fraud Detection dataset
- [Streamlit](https://streamlit.io/) for making ML apps effortless to build
- [Scikit-learn](https://scikit-learn.org/) for the robust ML toolkit
- The open-source Python community

---

<div align="center">
  <strong>AA · AI Fraud Detection System · Built by Areeb Ahsan · Powered by Machine Learning</strong>
</div>
