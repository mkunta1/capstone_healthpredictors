# Pro Analytics 02 Python Starter Repository

> Use this repo to start a professional Python project.

- Additional information: <https://github.com/denisecase/pro-analytics-02>
- Project organization: [STRUCTURE](./STRUCTURE.md)
- Build professional skills:
  - **Environment Management**: Every project in isolation
  - **Code Quality**: Automated checks for fewer bugs
  - **Documentation**: Use modern project documentation tools
  - **Testing**: Prove your code works
  - **Version Control**: Collaborate professionally

---

## WORKFLOW 1. Set Up Your Machine

Proper setup is critical.
Complete each step in the following guide and verify carefully.

- [SET UP MACHINE](./SET_UP_MACHINE.md)

---

## WORKFLOW 2. Set Up Your Project

After verifying your machine is set up, set up a new Python project by copying this template.
Complete each step in the following guide.

- [SET UP PROJECT](./SET_UP_PROJECT.md)

It includes the critical commands to set up your local environment (and activate it):

```shell
uv venv
uv python pin 3.12
uv sync --extra dev --extra docs --upgrade
uv run pre-commit install
uv run python --version
```

**Windows (PowerShell):**

```shell
.\.venv\Scripts\activate
```

**macOS / Linux / WSL:**

```shell
source .venv/bin/activate
```

---

## WORKFLOW 3. Daily Workflow

Please ensure that the prior steps have been verified before continuing.
When working on a project, we open just that project in VS Code.

### 3.1 Git Pull from GitHub

Always start with `git pull` to check for any changes made to the GitHub repo.

```shell
git pull
```

### 3.2 Run Checks as You Work

This mirrors real work where we typically:

1. Update dependencies (for security and compatibility).
2. Clean unused cached packages to free space.
3. Use `git add .` to stage all changes.
4. Run ruff and fix minor issues.
5. Update pre-commit periodically.
6. Run pre-commit quality checks on all code files (**twice if needed**, the first pass may fix things).
7. Run tests.

In VS Code, open your repository, then open a terminal (Terminal / New Terminal) and run the following commands one at a time to check the code.

```shell
uv sync --extra dev --extra docs --upgrade
uv cache clean
git add .
uvx ruff check --fix
uvx pre-commit autoupdate
uv run pre-commit run --all-files
git add .
uv run pytest
```

NOTE: The second `git add .` ensures any automatic fixes made by Ruff or pre-commit are included before testing or committing.

<details>
<summary>Click to see a note on best practices</summary>

`uvx` runs the latest version of a tool in an isolated cache, outside the virtual environment.
This keeps the project light and simple, but behavior can change when the tool updates.
For fully reproducible results, or when you need to use the local `.venv`, use `uv run` instead.

</details>

### 3.3 Build Project Documentation

Make sure you have current doc dependencies, then build your docs, fix any errors, and serve them locally to test.

```shell
uv run mkdocs build --strict
uv run mkdocs serve
```

- After running the serve command, the local URL of the docs will be provided. To open the site, press **CTRL and click** the provided link (at the same time) to view the documentation. On a Mac, use **CMD and click**.
- Press **CTRL c** (at the same time) to stop the hosting process.

### 3.4 Execute

This project includes demo code.
Run the demo Python modules to confirm everything is working.

In VS Code terminal, run:

```shell
uv run python -m analytics_project.demo_module_basics
uv run python -m analytics_project.demo_module_languages
uv run python -m analytics_project.demo_module_stats
uv run python -m analytics_project.demo_module_viz
```

You should see:

- Log messages in the terminal
- Greetings in several languages
- Simple statistics
- A chart window open (close the chart window to continue).

If this works, your project is ready! If not, check:

- Are you in the right folder? (All terminal commands are to be run from the root project folder.)
- Did you run the full `uv sync --extra dev --extra docs --upgrade` command?
- Are there any error messages? (ask for help with the exact error)

---

### 3.5 Git add-commit-push to GitHub

Anytime we make working changes to code is a good time to git add-commit-push to GitHub.

1. Stage your changes with git add.
2. Commit your changes with a useful message in quotes.
3. Push your work to GitHub.

```shell
git add .
git commit -m "describe your change in quotes"
git push -u origin main
```

This will trigger the GitHub Actions workflow and publish your documentation via GitHub Pages.

### 3.6 Modify and Debug

With a working version safe in GitHub, start making changes to the code.

Before starting a new session, remember to do a `git pull` and keep your tools updated.

Each time forward progress is made, remember to git add-commit-push.

# Health Insurance Risk Prediction

## Project Overview

This project aims to predict health insurance risk using patient, conditions, and immunizations datasets. The goal is to identify high-risk patients, understand healthcare utilization, and analyze factors driving healthcare costs.

Advanced analytics techniques are applied to clean, preprocess, and engineer features from raw healthcare data, followed by predictive modeling to forecast patient risk and insurance costs.

---

## 1. Data Sources

- **Patients:** Demographics including age, gender, race, ethnicity, marital status, and geographic information (city, county, state, ZIP, LAT, LON).
- **Conditions:** Clinical diagnoses, chronic conditions, start/stop dates.
- **Immunizations:** Vaccine types, dates, and costs.

Publicly available data is sourced from [Synthea Synthetic Health Data](https://github.com/synthetichealth/synthea-sample-data).

---

## 2. Data Cleaning & Preparation

### Columns to Keep
`BIRTHDATE`, `DEATHDATE`, `GENDER`, `RACE`, `ETHNICITY`, `MARITAL`, `CITY`, `COUNTY`, `BIRTHPLACE`, `STATE`, `ZIP`, `HEALTHCARE_EXPENSES`, `HEALTHCARE_COVERAGE`, `LAT`, `LON`.

### Columns to Drop
`Id`, `SSN`, `DRIVERS`, `PASSPORT`, `PREFIX`, `FIRST`, `LAST`, `SUFFIX`, `MAIDEN`, `ADDRESS`.

### Handling Missing Values
- **DEATHDATE:** Impute with placeholders (e.g., `9999-12-31`) or predictive imputation (regression/KNN).
- **MARITAL:** Use most frequent value or KNN imputation.
- **HEALTHCARE_EXPENSES:** Impute missing values using median/mean per age group or demographic.
- **ZIP, LAT, LON:** Ensure correct formats and numeric types.

### Date Standardization
- Convert `BIRTHDATE` and `DEATHDATE` to `datetime`.
- Conditions `START` and `STOP` dates standardized.
- Duration of each condition derived; flag active conditions.

### Feature Engineering
- Patient-level aggregates: number of conditions, number of active conditions, comorbidity index.
- Number of providers seen by a patient.
- Utilization intensity (high utilizers may indicate sicker patients).
- Geographic access (distance to providers).
- One-hot encode categorical features (`Gender`, `Race`, `Marital`, `City`).
- Detect outliers using IQR or Z-scores.

---

## 3. Exploratory Data Analysis (EDA)

### Demographic Insights
- Gender: roughly balanced between male and female.
- Race/Ethnicity: predominantly White and non-Hispanic.
- Age: skewed older; nearly half of patients aged 50+.
- Marital Status: over half married; 29% unknown.

### Geographic Insights
- All patients reside in Massachusetts; largest representation from Middlesex, Worcester, Suffolk counties.

### Healthcare Insights
- Patients with multiple chronic conditions have higher healthcare costs.
- Vaccination patterns vary by age and gender; pediatric compliance is highest, middle-aged adults lower, seniors increase again for flu/COVID.

---

## 4. Advanced Features

- Chronic condition counts and flags (diabetes, hypertension, heart disease, COPD/asthma, cancer).
- Active condition indicators.
- Number of vaccines received and unique vaccine types.
- Derived variables: age from birthdate, duration of conditions.
- Provider utilization intensity.
- Geographic access measures.
- Average healthcare expense by age group, gender, and race.

---

## 5. Predictive Modeling

- Combine patients + conditions + immunizations + procedures + medications to predict:
  - High-risk patients
  - Insurance costs
- Models used: Linear Regression, LASSO, Random Forest, Logistic Regression.

---

## 6. Data Preparation in VS Code

### Syntax Examples
```python
import pandas as pd

# Load CSV
patients1 = pd.read_csv('data/patients.csv')

# Inspect
print(patients1.head().to_string())
print(patients1.shape)
print(patients1.columns.tolist())
print(patients1.dtypes)

# Missing value analysis
missing_counts = patients1.isnull().sum()
missing_percent = patients1.isnull().mean() * 100

# Data type conversion
patients1['Age'] = patients1['Age'].astype(int)
patients1['Id'] = patients1['Id'].astype(str)
patients1['Gender'] = patients1['Gender'].astype('category')

# Frequency counts
freq = patients1['Gender'].value_counts(dropna=False)


Explain the cleaning requirements for your specific data.
Keep columns BIRTHDATE, DEATHDATE, GENDER, RACE, ETHNICITY,'MARITAL' , CITY, COUNTY, BIRTHPLACE, STATE, ZIP (with imputation), HEALTHCARE_EXPENSES, HEALTHCARE_COVERAGE, LAT ,  LON
Drop columns Id, SSN, DRIVERS, PASSPORT, PREFIX, FIRST, LAST, SUFFIX, MAIDEN, ADDRESS
handling missing values like DEATHDATE, Set STOP for conditons data to the date of data extraction.
Impute missing values like Deathdtate, placeholder like 9999-12-31, marital
BIRTHDATE, DEATHDATE  ==> standardzing date formats
Derive new variables: create age from birthdate, Age can be calculated based on the birthdate and today or deathdate - birthdate
Impute missing values for healthcare expenses.
LAT, LON: Ensure these are numeric form
check for the outliers in healthcare expenses.
date formats for start stop dates in conditions dataframe
derive duration based on start and stop dates
if the disease is continuing, then derive active condition variable
count number of diseases by patient.
handle overlapping coditions by patient

##feature engineering Number of Providers a Patient Has Seen

How can deathdate be apply predictive imputation techniques like regression or k-nearest neighbors (KNN) if there is sufficient data. MARITAL column can be imputed based on the most frequent value or use a statistical imputation method (like KNN imputation) to fill in the missing entries.

One-hot encoding for categorical data
use Interquartile Range (IQR) or Z-scores to detect and handle outliers.
Utilization intensity (patients seeing many providers with high utilization may be sicker).
Geographic access (distance to providers).
Average expense by age group, race, gender.
coverge analyssis. healthcare expenses vs healthcare_coverage
most common diagnosis in the population
identify high-risk patients with multiple conditions.



Predictive modeling of healthcare risk

Use patients + conditions + procedures + medications + immunizations + demographics to predict high-risk patients or insurance costs.

Healthcare utilization analysis

Combine encounters + procedures + imaging + devices + careplans to see which patients consume the most resources.



### Summary on patients data
Demographic Insights

The patient population is evenly split between males and females, ensuring gender-balanced modeling. The racial and ethnic composition is predominantly White and non-Hispanic, which reflects the Massachusetts population but reduces demographic diversity. This limitation may affect generalizability to more diverse populations.

Geographic Insights

All patients reside within Massachusetts, with the largest representation from Middlesex, Worcester, and Suffolk counties. This enables county-level geographic analysis even though ZIP code data is partially missing.

Marital Status

Over half of the patients are married, while 29% have unknown marital status. This missingness is likely systemic and should be handled using an “Unknown” category during modeling.

Age Distribution

The dataset is older-skewed, with nearly half of the patients aged 50 and above. Because older adults have higher healthcare utilization and chronic disease rates, age is expected to be a key predictor in risk modeling.

A single subplot with all demographics combined (stacked bars)

## Further steps

✔ Demographic analysis --> Age vs healthcare cost, Gender differences in conditions, Race/ethnicity differences in immunizations

✔ Geographic analysis --> County-level heatmaps, Average cost per county, Condition prevalence per county

✔ Predictive modeling --> Use age, gender, race, immunizations, and chronic conditions to predict, high-risk vs low-risk, healthcare expenses
I need next steps of preparing data in vs code for patients, conditions and immunizations datasets

## syntax:
-- To count the frequency value_counts(),  dropna=False argument ensures that missing values (NaN) are also counted. freq = df['Gender'].value_counts()
-- find the data type: patients2.dtypes ==> This shows each column and its type (int64, float64, object, datetime64[ns], etc.).
import pandas as pd
-- read file as csv ==> patients1 = pd.read_csv('C:\\Users\\Mahi2\\capstone\\capstone_healthpredictors\\data\\patients.csv')
-- gives first few rows in a dataframe: print(patients1.head().to_string()) => Converts the DataFrame into a plain text string
-- gives number of rows and columns: patients1.shape ==> Returns a tuple (rows, columns)
-- gives columns as a list : patients1.columns.tolist() ==> gives columns []
-- slice first 8 characters in a column: patients1['Id'].str[:8] ==> slices the first 8 characters here.
-- Handling Missing Values: missing_counts = patients1.isnull().sum()
missing_percent = patients1.isnull().mean() * 100
-- patients2 = patients1.copy()
-- convert to integer: df['Age'] = df['Age'].astype(int)
-- convert to string : df['Id'] = df['Id'].astype(str)
-- convert to float : df['Age'] = df['Age'].astype(float)
-- convert to category : df['Gender'] = df['Gender'].astype('category')


# Example data
data = {
    'Id': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22],
    'Gender': ['F', 'M', 'M']
}

# Create DataFrame
df = pd.DataFrame(data)

