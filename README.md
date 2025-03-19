## Project Overview

This project aims to predict whether a heart failure patient will survive (`DEATH_EVENT = 0`) or not (`DEATH_EVENT = 1`) based on clinical data.

Heart failure is a serious condition, and early prediction can help doctors provide better treatments.  
By using **machine learning classification models**, I can analyze patterns in medical data and improve decision-making.

I compare **three classification models**:

- **Decision Tree**
- **Random Forest**
- **Logistic Regression**

The best-performing model is **Logistic Regression** in terms of overall metrics.  
However, since Recall is the most important metric in this case, Random Forest performed just as well as Logistic Regression, both achieving a recall score of 0.79.  
Therefore, Random Forest is also a strong candidate.

## Dataset

### License

The dataset is licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**.

### Attribution

- **Original Dataset Author:** Larxel
- **Source:** [Kaggle Dataset Link](https://www.kaggle.com/datasets/andrewmvd/heart-failure-clinical-data/data?select=heart_failure_clinical_records_dataset.csv)
- **License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

### Description

| Column                     | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| `age`                      | Age of the patient                                        |
| `anaemia`                  | Decrease of red blood cells (0: No, 1: Yes)               |
| `creatinine_phosphokinase` | Level of CPK enzyme in blood (mcg/L)                      |
| `diabetes`                 | If the patient has diabetes (0: No, 1: Yes)               |
| `ejection_fraction`        | Percentage of blood leaving the heart at each contraction |
| `high_blood_pressure`      | If the patient has hypertension (0: No, 1: Yes)           |
| `platelets`                | Platelet count in the blood (kiloplatelets/mL)            |
| `serum_creatinine`         | Level of creatinine in the blood (mg/dL)                  |
| `serum_sodium`             | Level of sodium in the blood (mEq/L)                      |
| `sex`                      | Gender of the patient (0: Female, 1: Male)                |
| `smoking`                  | If the patient smokes (0: No, 1: Yes)                     |
| `time`                     | Follow-up period (days)                                   |
| `DEATH_EVENT`              | Target variable (0: No, 1: Yes)                           |

## 🔬 Model Training Process

1. **Data Preprocessing**

   - Handle missing values (if any)
   - Normalize numerical features

2. **Feature Selection**

   - Analyze feature importance using correlation heatmaps
   - Remove unnecessary or redundant features

3. **Model Training**

   - Train three classification models: **Decision Tree, Random Forest, Logistic Regression**
   - Use **GridSearchCV** for hyperparameter tuning

4. **Evaluation Metrics**
   - Accuracy, Precision, Recall, F1-score
   - ROC-AUC for final model selection

## Links

- **Dataset:** [heart_failure_clinical_records_dataset.csv](data/heart_failure_clinical_records_dataset.csv)
- **Notebook:** [heart-failure-classification](heart-failure-classification.ipynb)
