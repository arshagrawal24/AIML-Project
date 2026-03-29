# AI Real Estate Price Prediction Engine

A beginner-friendly **Machine Learning project** that predicts house prices based on property features using **Linear Regression**.

---

## Project Description

This project is a command-line based AI system that:

* Loads housing data from a dataset
* Trains a machine learning model
* Evaluates its performance
* Predicts house prices based on user input

It simulates a simple **AI-powered real estate prediction engine**.

---

##  Features

*  Data cleaning (removes missing values)
*  Machine Learning using Linear Regression
*  Model evaluation (R² Score & MAE)
*  Interactive user input system
*  Multiple predictions in one run

---

##  Dataset Requirements

The project uses a CSV file named:

```bash id="z8plx1"
Dataset.csv
```

Your dataset must include the following columns:

```text id="kdl7d3"
Area, BHK, Bathroom, Parking, Per_Sqft, Price
```

---

##  Model Details

* Algorithm: **Linear Regression**
* Train/Test Split: 80% / 20%
* Metrics:

  * R² Score (accuracy)
  * Mean Absolute Error (MAE)

---

##  How to Run

### 1. Install dependencies

```bash id="q9kkgm"
pip install pandas scikit-learn
```

### 2. Run the program

```bash id="zq4k2o"
python Main.py
```

---

##  How It Works

1. Loads dataset
2. Cleans missing data
3. Selects important features:

   * Area
   * BHK
   * Bathrooms
   * Parking
   * Price per sq ft
4. Trains Linear Regression model
5. Evaluates model performance
6. Takes user input for prediction

---

##  Sample Output

```text id="8w2yfx"
AI REAL ESTATE PREDICTION ENGINE ONLINE

Enter Property Specifications:
Area: 1200
BHK: 3
Bathroom: 2
Parking: 1
Per Sq Ft: 5000

ESTIMATED MARKET VALUE: ₹60,00,000
```

---

##  Output Metrics

* **R² Score** → Model accuracy
* **MAE** → Average prediction error

---

##  Future Improvements

* Add GUI (Tkinter / Web App)
* Use advanced models (Random Forest, XGBoost)
* Deploy as a web application

---

##  Author

**Arsh Agrawal**
Course: Fundamentals of AIML
Institution: VIT Bhopal
Submission: BYOP — VITyarthi Platform

---
