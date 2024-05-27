# Project Summaries

## Project 1: Diabetes Prediction
- **Dataset:** [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Objective:** Predict the onset of diabetes based on diagnostic measures.
- **ML Algorithms:** Logistic Regression, Support Vector Classifier (SVC), XGBoost Classifier, Random Forest Classifier
- **Decision:** 
  - In this dataset, we aim to identify diabetic and non-diabetic instances. Reducing false negatives is more important as predicting a person as non-diabetic when they are diabetic could lead to delays in treatment, monitoring, and serious health issues.
  - Therefore, recall is more important; hence, XGBClassifier seems the most appropriate model.

## Project 2: Sales Prediction
- **Objective:** Apply necessary ML algorithms for the given dataset. Evaluate the model using one feature and multiple features.
- **ML Algorithms:** Linear Regression, Lasso, Ridge, SVR
- **Decision:**
  - Based on the evaluation metrics, simple linear regression or regularized regression techniques like Lasso and Ridge are suitable for this dataset. SVR might not be the best choice in terms of prediction accuracy.
  - Lasso Regression is recommended.

## Project 3: Employee Attrition Prediction
- **Objective:** Handle the missing data in the given dataset and create 2 ML models and compare them.
- **ML Algorithms:** Logistic Regression, SVM
- **Decision:**
  - The Logistic Regression model outperforms the SVM model in terms of accuracy, precision, recall, and F1-score for both classes.
  - The Logistic Regression model has higher precision, recall, and F1-score for predicting both classes.
  - The SVM model has lower accuracy and performs relatively poorer in terms of precision, recall, and F1-score for both classes compared to the Logistic Regression model.
  - Both models have similar support values and confusion matrix structures, but the Logistic Regression model makes fewer incorrect predictions overall.

## Project 4: Water Quality Prediction
- **Dataset:** [Water Potability dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)
- **Objective:** Predict the quality of water using two classification algorithms.
- **ML Algorithms:** Random Forest Classifier, Gradient Boosting Classifier
- **Decision:**
  - Although both models have similar overall accuracy, the Random Forest Classifier tends to have a better balance between precision and recall for both classes. Additionally, its precision for class 0 (non-potable water) is slightly higher, making it the preferred model.
