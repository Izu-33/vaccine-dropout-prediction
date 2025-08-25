# Vaccine Dropout Prediction

This project develops a machine learning model to predict vaccine dropout risk (DTP1–DTP3) across African countries using immunization and demographic data.  
It also includes an interactive **Streamlit app** for real-time predictions.

---

## 🚀 Features
- Preprocessing pipeline with scaling, encoding, and SMOTE for class balance  
- Models trained with **Logistic Regression, Random Forest, SVM, and XGBoost** using GridSearchCV  
- Automatic region selection when a user chooses a country  
- Streamlit dashboard with metric cards (**Dropout Rate, Coverage Average, DTP3 Coverage**)  
- Visualizations including boxplots and interactive charts  

---

## 📂 Project Structure
```bash
├── data/ # Raw and processed datasets
├── notebooks/ # Jupyter notebooks for exploration & training
├── app/ # Streamlit app
│ ├── app.py
│ └── utils.py
├── models/ # Saved models and preprocessing pipelines
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```

## ⚙️ Installation

Clone this repo:
```bash
git clone https://github.com/your-username/vaccine-dropout-prediction.git
cd vaccine-dropout-prediction
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Run Streamlit app
```bash
streamlit run app/app.py
```

## 📊 Example App View

- Metric cards for Dropout Rate, Coverage Average, DTP3 Coverage
- Country & region selection with automatic region mapping
- Prediction probability shown with visual feedback

## 📌 Future Improvements

- Deploy on Streamlit Cloud or Azure Web App
- Add additional health & socioeconomic predictors
- Expand dataset beyond Africa

