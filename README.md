# 🩺 Chronic Kidney Disease Prediction Using Machine Learning

This project aims to build a predictive machine learning model that determines the likelihood of a patient having **Chronic Kidney Disease (CKD)** based on various clinical features. The model uses supervised classification techniques and is deployed with a user-friendly interface.

---

## 📂 Dataset Information

- **Dataset Name:** `kidney_disease.csv`  
- **Records:** 400  
- **Features:** 26 (Numerical + Categorical)  
- **Target Variable:** `classification` (values: `ckd`, `notckd`)

### 🔢 Numerical Features:
- age (years)
- bp (blood pressure, mmHg)
- sg (specific gravity)
- al (albumin)
- su (sugar)
- bgr (blood glucose random, mg/dL)
- bu (blood urea, mg/dL)
- sc (serum creatinine, mg/dL)
- sod (sodium, mEq/L)
- pot (potassium, mEq/L)
- hemo (hemoglobin, g/dL)
- pcv (packed cell volume)
- wc (white blood cell count)
- rc (red blood cell count)

### 🔠 Categorical Features:
- rbc (red blood cells: normal/abnormal)
- pc (pus cell: normal/abnormal)
- pcc (pus cell clumps: present/not present)
- ba (bacteria: present/not present)
- htn (hypertension: yes/no)
- dm (diabetes mellitus: yes/no)
- cad (coronary artery disease: yes/no)
- appet (appetite: good/poor)
- pe (pedal edema: yes/no)
- ane (anemia: yes/no)

---

## 🧪 Machine Learning Pipeline

### 🔧 Data Preprocessing:
- Handling missing values (mean/median/mode imputation)
- Encoding categorical features (Label Encoding / One-Hot Encoding)
- Feature scaling (MinMaxScaler)
- Outlier removal using statistical methods

### 🧠 Models Trained:
- Logistic Regression  
- Decision Tree  
- Random Forest  
- K-Nearest Neighbors (KNN)  
- Support Vector Machine (SVM)  
- Naive Bayes  
- XGBoost  
- Voting Classifier (Ensemble)

---

## 📊 Model Evaluation Metrics
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC-AUC  
- Confusion Matrix & Heatmap

---

## 🚀 How to Run the Project Locally

### 1. Clone the repository:
```bash
git clone https://github.com/saisubbaraom2003/Chronic-Kidney-Disease-Prediction.git
cd Chronic-Kidney-Disease-Prediction
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Train the model:
```bash
python src/train.py
```
4. Evaluate the model:
```bash
python src/evaluate.py
```
5. (Optional) Run the web application:
```bash
streamlit run app/app.py
```
🌐 Live Demo
You can view the live demo of the Kidney Disease Prediction Model [here](https://ckd-a17m.onrender.com).

🛠️ Tech Stack
Languages & Libraries: Python 3.x, Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn

Deployment: Streamlit / Flask (local or cloud-based: AWS, Azure, Render)

Version Control: Git & GitHub

📈 Future Enhancements
Hyperparameter tuning for better accuracy

Cross-validation strategies

Cloud deployment (AWS/GCP) with CI/CD pipelines

Model interpretability (SHAP, LIME)

🤝 Contributions
Pull requests are welcome!
For major changes, open an issue first to discuss your suggestions.

📄 License
This project is licensed under the MIT License.

📬 Contact
For any queries or feedback:
📧 sai.subbu.in@gmail.com

Author: Sai Subba Rao Mahendrakar
📅 Date: 26 February 2025
