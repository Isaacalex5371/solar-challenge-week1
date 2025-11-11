# 📓 Solar Challenge – Notebooks Overview

This folder contains the **Jupyter notebooks** used for exploring, cleaning, and analyzing solar irradiance datasets for multiple West African countries.  

Each notebook represents a stage of the data pipeline — from raw input to cleaned, analysis-ready datasets.

---

## 📘 Notebook List

### 🟢 `benin_eda.ipynb`
**Status:** ✅ Completed  
**Dataset:** `data/benin-malanville.csv`  
**Output:** `data/benin_clean.csv`  

#### Key Steps:
- Loaded and explored the Benin dataset  
- Parsed timestamps and removed invalid entries  
- Checked for missing data and handled them properly  
- Detected and removed outliers using z-score  
- Exported the cleaned dataset for later comparison  

---

### 🟡 `sierra_leone_eda.ipynb`
**Status:** ⏳ Pending (Template Ready)  
**Dataset:** `data/sierra_leone_raw.csv` *(to be added)*  
**Output:** `data/sierra_leone_clean.csv`

#### Notes:
- Uses the same structure and logic as the Benin notebook  
- Simply replace file paths with Sierra Leone dataset names once available  
- Run all cells to produce the cleaned output  

---

### 🟡 `togo_eda.ipynb`
**Status:** ⏳ Pending (Template Ready)  
**Dataset:** `data/togo_raw.csv` *(to be added)*  
**Output:** `data/togo_clean.csv`

#### Notes:
- Follows identical steps to Benin and Sierra Leone  
- Make sure timestamps and column names match your dataset  

---

### 🔵 `compare_countries.ipynb`
**Status:** 🧩 In Progress  
**Purpose:**  
Merges all available cleaned datasets for multi-country analysis and visualization.

#### Features:
- Dynamically loads available `_clean.csv` files  
- Handles missing datasets gracefully (prints warnings)  
- Produces regional irradiance comparison plots  

---

## 🧠 How to Use
1. Open any `.ipynb` file in **VS Code** or **Jupyter Lab**  
2. Run all cells sequentially  
3. Check the `/data/` folder for generated cleaned files  

---

## 💡 Tip for Developers
If you add a new dataset (e.g. Ghana), just:
1. Copy one of the existing notebooks  
2. Rename it (`ghana_eda.ipynb`)  
3. Update the file paths inside  
4. Add your new cleaned file to the comparison notebook  

---

## 👨🏾‍💻 Author
**Yishak Alemayehu (Isaacalex5371)**  
Solar Challenge – Week 1 Contributor  
GitHub: [@Isaacalex5371](https://github.com/Isaacalex5371)

