# Walmart Weekly Sales Forecast – Dept 6

---

## 📌 Overview

This project forecasts weekly sales for **Walmart Department 6** using various time series modeling techniques, including:

- Traditional Statistical Models
- Machine Learning
- Deep Learning
- Facebook Prophet
- Innovative Neural Architecture: **N-BEATS**

The goal is to compare model performance, extract meaningful business insights, and deploy the best model using **Streamlit**.

---

## 🧠 Problem Statement

Walmart wants to improve inventory and staffing decisions by predicting **weekly sales** at the department level.  
Your task: Forecast sales for **Department 6** using historical data, trends, seasonality, holidays, and external variables.

---

## 📂 Project Structure
- `notebooks/` – full EDA + modeling
- `models/` – saved best model (Random Forest)
- `app/` – Streamlit app for prediction
- `data/` – cleaned CSV
- `assets/` – images for presentation

---


---

## 🛠️ Tools & Technologies

- Python, Pandas, NumPy
- Scikit-learn (Random Forest, XGBoost)
- Statsmodels (ARIMA/SARIMA)
- Facebook Prophet
- TensorFlow/Keras (LSTM, GRU)
- NeuralForecast (N-BEATS)
- Streamlit (Deployment)
- Matplotlib, Seaborn (Visualization)

---

## 📈 Models Compared

| Model           | RMSE     | MAE      | Notes                                |
|----------------|----------|----------|---------------------------------------|
| **Random Forest** | **953.48**  | **600.77**  | ✅ Best overall performance |
| XGBoost         | 1039.55  | 685.07   | Solid tree-based learner              |
| Holt-Winters    | 1218.28  | 838.93   | Great seasonal baseline               |
| N-BEATS         | 1358.66  | 863.74   | 🧪 Novel deep learning model           |
| GRU             | 1290.93  | 811.94   | Performs well, but not best           |
| LSTM            | 1328.48  | 876.29   | Requires more data                    |
| SARIMA          | 1512.19  | 1254.11  | Traditional but weaker                |
| ARIMA           | 2086.53  | 1837.19  | ❌ Worst among classical models        |
| Prophet         | 6068.62  | 5318.17  | ❌ Good visuals, poor accuracy         |

---

## 🏆 Best Model

> ✅ **Random Forest Regressor**  
> - RMSE: `953.48`  
> - MAE: `600.77`  
> - Selected for deployment via Streamlit

---

## 🚀 Streamlit App (Local Deployment)

### 🔧 Prerequisites

```bash
pip install -r requirements.txt

---
## 🚀 Run the App
```bash
streamlit run app/main.py

