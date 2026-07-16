# 🎓 Student Performance Prediction

A Machine Learning project that predicts students' final grades (G3) using demographic, social, and academic features.

---

## 📌 Project Overview

The goal of this project is to predict the final mathematics grade (G3) of students using different Machine Learning models and compare their performance.

---

## 📂 Dataset

- Dataset: Student Performance Dataset
- Subject: Mathematics
- File Used: `student-mat.csv`

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📊 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Data Overview
- Missing Values Check
- Duplicate Check
- Statistical Summary
- Correlation Analysis
- Distribution Analysis
- Boxplots
- Scatter Plots
- Outlier Detection

---

## 🤖 Machine Learning Models

Three regression models were trained and evaluated:

- Linear Regression
- Lasso Regression
- Random Forest Regressor

---

## 📈 Model Performance

| Model | MAE | RMSE | R² Score |
|-------|------|------|---------|
| Linear Regression | 1.65 | 2.38 | 0.72 |
| Lasso Regression | 1.38 | 2.16 | 0.77 |
| Random Forest | **1.18** | **1.96** | **0.82** |

### 🏆 Best Model

Random Forest Regressor achieved the best performance with an R² score of **0.82**.

---

## 📁 Project Structure

```
student-performance-prediction/
│
├── data/
├── images/
├── models/
├── notebooks/
├── src/
├── README.md
└── requirements.txt
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone <(https://github.com/x3ZAB/student-performance-prediction.git)>
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook inside:

```
notebooks/student_performance.ipynb
```

---

## 📷 Project Visualizations

The project includes several visualizations:

- Correlation Heatmap
- Target Distribution
- Study Time vs Final Grade
- Failures vs Final Grade
- Actual vs Predicted
- Error Distribution

---

## 📌 Future Improvements

- Hyperparameter Tuning
- Feature Selection
- XGBoost Regression
- LightGBM Regression
- Model Deployment with Streamlit
