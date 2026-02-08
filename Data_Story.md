Title: Uncovering the "Unsinkable" – A Titanic Data Journey

The Challenge We started with a raw manifest of passengers from the Titanic (train.csv). Our goal was not just to look at the list, but to understand who survived and why, and to build a tool that could predict survival based on passenger characteristics.

The Cleanup (Making Sense of the Chaos) The raw data was messy—much like the event itself. We found gaps in the records:

The "Cabin" Mystery: Most cabin numbers were missing. Rather than guessing, we removed this data point to prevent misleading our analysis.
The Age Gap: We had passengers with no recorded age. Instead of discarding them, we applied the "median age" of the group to fill these gaps, ensuring we didn't lose valuable data points.
Standardization: We fixed messy text entries, ensuring "male" wasn't recorded as "male " (with a space) or "MALE", creating a consistent standard.
The Discovery (Feature Engineering) We dug deeper than the surface-level columns:

Status Matters: By extracting titles like "Mr.", "Mrs.", and "Master" from names, we gained insight into social standing and gender roles beyond just "Sex".
Strength in Numbers?: We calculated family size. We asked: "Did traveling alone help or hurt?" We created an IsAlone indicator to test this.
The Cost of Safety: We grouped fares into categories (Low, Mid, High, Very High). This revealed clear distinctions in survival rates based on economic class.
The Prediction (The Model) We fed this refined "fuel" into a Logistic Regression model. Think of this as a mathematical calculator that weighs every factor—Age, Class, Gender, Family Size—to output a probability.

The Result Our model successfully predicts passenger survival with about 80% accuracy.

Key Drivers: The analysis confirmed that Sex (Women), Class (1st Class), and Age (Children) were the strongest predictors of survival.
Business Value: We now have a clean, enriched dataset (cleaned_titanic.csv) stored in our database, ready for dashboarding or further predictive analytics. We moved from a messy spreadsheet to a predictive asset.