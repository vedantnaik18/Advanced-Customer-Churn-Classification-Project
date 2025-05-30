# Advanced-Customer-Churn-Classification-Project
Advanced Customer Churn Classification Project

Project Objective  
This project aims to predict customer churn for a telecom company using customer demographic and service usage data. By identifying customers at high risk of churn, the company can proactively implement targeted retention strategies to reduce financial loss and improve customer satisfaction.

Dataset Summary  
1. Total Customers: 7,043  
2. Data Includes:  
   - Demographic details (gender, senior citizen status, etc.)  
   - Usage patterns (internet service, online security, contract type, etc.)  
3. Churn Rate: Approximately 26.5%, indicating a significant opportunity for customer retention.

Key Insights from Exploratory Data Analysis (EDA)  
1. Customers with month-to-month contracts have a much higher churn rate than those with long-term contracts.  
2. Lack of online security or tech support is associated with higher churn.  
3. Higher monthly charges are strongly linked to churn.  
4. MonthlyCharges and TotalCharges are positively correlated (ρ = 0.65).  
5. Customers without partners or dependents are more likely to churn.

Modeling Approach  
1. Multiple models tested: Logistic Regression, Random Forest, and XGBoost.  
2. Feature engineering included:  
   - Creation of variables like `IsFamily`.  
   - Encoding categorical features.  
   - Handling missing values.  
3. Hyperparameter tuning applied using GridSearchCV.

Final Results (Tuned XGBoost)  
1. Accuracy: 73%  
2. Precision: 49%  
3. Recall (Churn class): 80%  
4. F1-score: 0.61  
5. ROC AUC: 0.84 ✅  

*The model is optimized for high recall to ensure most churn-prone customers are identified, even if it means slightly lower precision.*

Business Impact  
1. Identify at-risk customers and trigger retention offers (discounts, loyalty rewards).  
2. Prioritize outreach to customers with short-term contracts or lacking support services.  
3. Bundle high-risk services (like online security) to reduce churn.

Strategic Recommendations  
1. Offer incentives to convert month-to-month contracts to longer-term ones.  
2. Launch proactive support for users without tech help or online security.  
3. Use personalized offers based on churn risk score to retain valuable customers.  
4. Integrate the model in CRM systems via API to flag churn risk in real-time.  
