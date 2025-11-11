

#  Solar Irradiance Data Pipeline – Week 0

This repository contains the **Week 0 deliverable** for the Solar Challenge Project.
It focuses on **data loading, cleaning, and exploratory data analysis (EDA)** for multiple West African solar datasets — including **Benin, Sierra Leone, and Togo**.

---

##  Repository Structure

```
solar-week1-/
│
├── .github/workflows/
│   └── ci.yml                 # Continuous Integration workflow
│
├── data/                      # Raw and cleaned datasets
│   ├── benin-malanville.csv
│   ├── sierraleone-bumbuna.csv
│   ├── togo-dapaong_qc.csv
│   └── benin_clean.csv
│
├── notebooks/                 # Jupyter notebooks for EDA
│   ├── benin_eda.ipynb
│   ├── sierraleone_eda.ipynb
│   ├── togo_eda.ipynb
│   └── README.md
│
├── src/                       # Source code modules
│   ├── data_loader.py         # Handles dataset loading and path management
│   └── preprocessing.py       # Data cleaning, imputation, and transformation functions
│
├── tests/                     # Unit tests
│   ├── test_preprocessing.py  # Tests for preprocessing functions
│   └── __init__.py
│
├── scripts/                   # Placeholder for future automation scripts
│
├── .gitignore
├── requirements.txt            # Python dependencies
└── README.md                   # Project overview
```

---

## ⚙️ Key Features

* Modularized data pipeline with reusable functions:

  * **Data loading** (`src/data_loader.py`)
  * **Preprocessing & cleaning** (`src/preprocessing.py`)
  * **EDA notebooks** for each region under `notebooks/`
* **Automated CI** setup with GitHub Actions (`.github/workflows/ci.yml`)
* Early **unit testing** included under `tests/`

---

## 🧠 Design & Code Organization

Keeping the logic inside the `src/` directory helps maintain:

* Reusability across multiple country datasets
* Cleaner notebooks focused on visualization and interpretation
* Easier integration into future automated pipelines

---

## 🚀 How to Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Isaacalex5371/solar-challenge-week1.git
   cd solar-challenge-week1
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   venv\Scripts\activate    # On Windows
   source venv/bin/activate # On Mac/Linux
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run Jupyter Notebook:**

   ```bash
   jupyter notebook notebooks/benin_eda.ipynb
   ```
