# Machine Learning–based Thyroid Cancer Recurrence Prediction System built using Streamlit and Scikit-learn.

This application predicts whether a patient is at **high or low risk of recurrence** based on structured clinical features.

---
## 🌐 Live Demo

[🚀 Try the Live App](https://thyroid-cancer-recurrence-using-ml.onrender.com)

Deployed on Render using Streamlit.

---

## Model Performance

**Best Hyperparameters**
- `n_estimators = 100`
- `max_depth = None`
- `min_samples_split = 2`

**Evaluation Metrics**

- Accuracy: **0.96**
- ROC-AUC Score: **0.99**
- Weighted F1-Score: **0.96**

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|-------|----------|--------|----------|---------|
| No    | 0.95     | 1.00   | 0.97     | 55      |
| Yes   | 1.00     | 0.86   | 0.93     | 22      |

---

## Tech Stack

- Python
- Scikit-learn
- Streamlit
- Pandas
- Joblib

---

## Project Structure

```
OncoPredict-Thyroid/
│
├── app.py
├── model.pkl
├── requirements.txt
└── README.md
```

---

# Installation & Setup

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/OncoPredict-Thyroid.git
cd OncoPredict-Thyroid
```

## 2. Create Virtual Environment

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the Application

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## ⚠️ Disclaimer

This project is developed for educational and research purposes only.  
It is not intended for real-world medical diagnosis.
