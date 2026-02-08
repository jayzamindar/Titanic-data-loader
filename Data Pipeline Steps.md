# Data Pipeline Steps

### 1. Data Cleaning & Preprocessing
We performed a rigorous cleaning process to ensure data quality:
- **Handling Missing Values**:
  - **Cabin**: Dropped due to excessive missing data.
  - **Age**: Missing values filled with the median age to maintain distribution.
  - **Embarked**: Filled with the mode (most common port).
  - **Fare**: Filled with the median fare.
- **Row Filtering**: Dropped rows where critical information (Name, Sex, Ticket, Pclass, Survived) was missing.
- **Text Standardization**: Corrected capitalization and spacing in object columns (Name, Ticket, etc.).

### 2. Feature Engineering
To improve model performance, we created new features from existing data:
- **`Title`**: Extracted from passenger names (e.g., Mr., Mrs., Miss) to capture social status.
- **`FamilySize`**: Calculated as `SibSp` (Siblings/Spouses) + `Parch` (Parents/Children) + 1.
- **`IsAlone`**: A binary flag indicating if the passenger was traveling solo.
- **`FareBin` & `AgeBin`**: Grouped continuous variables into categories (e.g., "Young Adult", "High Fare") to help the model find patterns.
- **Encoding**: Converted categorical variables (`Sex`, `Embarked`) into numeric codes (`Sex_code`, `Embarked_code`) for machine learning.

### 3. Modeling & Evaluation
- **Model**: Logistic Regression.
- **Target**: `Survived` (0 = No, 1 = Yes).
- **Features Used**: Pclass, Sex_code, Age, Fare, FamilySize, IsAlone, Embarked_code.
- **Performance**: The model achieved an accuracy of approximately **80%** on the test set.