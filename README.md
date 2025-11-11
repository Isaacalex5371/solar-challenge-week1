

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


```markdown
# 🌞 Solar Challenge – Week 0 (Challenge 3)

This repository contains the **Week 0 submission** for the Solar Irradiance Data Pipeline Challenge.  
The goal of this challenge is to **load, clean, and analyze solar irradiance datasets** for multiple West African regions — beginning with **Benin**, and later expanding to **Sierra Leone** and **Togo**.

---

## 📁 Repository Structure

```

solar-challenge-week0/
│
├── .github/
│   └── workflows/
│       └── ci.yml                  # Continuous Integration setup
│
├── notebooks/
│   ├── **init**.py
│   ├── benin_eda.ipynb             # Data cleaning and exploration for Benin
│   ├── sierra_leone_eda.ipynb      # (Template – coming soon)
│   ├── togo_eda.ipynb              # (Template – coming soon)
│   └── README.md                   # Notebook-level documentation
│
├── scripts/                        # Python scripts (if needed)
│
├── src/                            # Source code for modular data pipeline
│
├── tests/                          # Test scripts
│
├── venv/                           # Virtual environment (ignored by git)
│
├── data/
│   ├── benin-malanville.csv         # Raw data
│   ├── benin_clean.csv              # Cleaned data
│   ├── sierra_leone_clean.csv       # Placeholder (to be added)
│   ├── togo_clean.csv               # Placeholder (to be added)
│   └── README.md                    # Data dictionary & notes
│
├── .gitignore
├── requirements.txt
└── README.md                       # ← you are here

```

---

## 🧹 Task Breakdown

### ✅ Task 1 – Benin Data Cleaning  
- Loaded the **Benin (Malanville)** dataset  
- Checked for **missing values, duplicates, and outliers**  
- Converted timestamp columns to `datetime`  
- Cleaned invalid or extreme irradiance readings  
- Exported cleaned file as:  
```

data/benin_clean.csv

````

### 🔄 Task 2 – Prepare for Multi-Country Pipeline  
- Created **template cleaning notebooks** for:
- Sierra Leone → `notebooks/sierra_leone_eda.ipynb`
- Togo → `notebooks/togo_eda.ipynb`
- Added placeholder files:
- `data/sierra_leone_clean.csv`
- `data/togo_clean.csv`
- Updated the **comparison notebook** to handle missing datasets gracefully

---

## 🧰 Setup Instructions

1. **Clone the repository**
 ```bash
 git clone https://github.com/Isaacalex5371/solar-challenge-week1.git
 cd solar-challenge-week1
````

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate    # (Linux/Mac)
   venv\Scripts\activate       # (Windows)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run notebooks**
   Open any `.ipynb` file under `/notebooks/` using **VS Code** or **Jupyter Lab**.

---

## 🧪 CI Workflow

GitHub Actions automatically runs:

* Lint checks (`flake8`, `black`)
* Notebook execution tests (using `pytest`)

Defined under:

```
.github/workflows/ci.yml
```

---

## 📊 Next Steps

* Add raw datasets for **Sierra Leone** and **Togo**
* Complete their cleaning and visualization notebooks
* Merge all cleaned data for regional irradiance comparison

---

## 👨🏾‍💻 Author

**Yishak Alemayehu (Isaacalex5371)**

GitHub: [@Isaacalex5371](https://github.com/Isaacalex5371)

---
