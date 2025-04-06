# **Credit Risk Assessment**

### **Problem Statement:**

Financial institutions face significant challenges in accurately assessing the credit risk of potential borrowers. Traditional credit scoring models may not fully capture the complexities of borrower behavior, leading to suboptimal lending decisions. This project aims to develop a machine learning application that utilizes ensemble learning techniques to enhance the prediction accuracy of credit risk, thereby aiding financial institutions in making informed lending decisions.

### **Dataset:**

Detailed data description of Credit Risk dataset:

- **person_age:** Age
- **person_income:** Annual Income
- **person_home_ownership:** Home ownership
- **person_emp_length:** Employemnt length (in years)
- **loan_intent:** Loan Intent
- **loan_grade:** Loan grade
- **loan_amnt:** Loan amount
- **loan_int_rate:** Interest rate
- **loan_status:** Loan status (0 is non default, 1 is default)
- **loan_percent_income:** Percent income
- **cb_person_on_file:** Historical default
- **cb_person_cred_hist_length:** Credit history length

### **Tech Stack:**

- **Backend Framework:** Python
- **Machine Learning Libraries:** Pandas, Scikit-learn, XGBoost

### **Implementation Steps:**

1. **Step 1: Data Preparation**
   - Collect and preprocess the dataset, ensuring it is suitable for modeling.
   - Perform exploratory data analysis to understand feature distributions and relationships.

2. **Step 2: Model Training and Evaluation**
   - Train multiple ensemble models and evaluate their performance using cross-validation.
   - Tune hyperparameters to optimize model accuracy and robustness.

### **Uniqueness and Impact:**

By focusing on ensemble learning techniques, this project aims to improve the accuracy and reliability of credit risk assessments. Accurate credit risk prediction is crucial for financial institutions to minimize defaults and maintain profitability.

### **Insights Gained:**

Based on exploratory data analysis and model interpretation, the following features were identified as the most influential in determining a person's credit risk:

- **Loan Interest Rate:** Higher interest rates are strongly associated with increased credit risk.
- **Loan Percent Income:** The proportion of the loan amount relative to a borrower's income is a critical indicator of repayment ability.
- **Loan Grade:** Loans with lower grades (e.g., D or F) are significantly more likely to be risky.
- **Historical Defaults:** Borrowers with a history of defaults tend to exhibit a higher likelihood of credit risk.

These insights can inform more accurate credit policies and help reduce financial risk for lenders.