from django import forms

class CreditRiskForm(forms.Form):
    # Define choice fields
    loan_grade_choices = (("A","A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"), ("F", "F"))
    loan_intent_choices = (("DEBTCONSOLIDATION", "Debt Consolidation"), ("EDUCATION", "Education"), ("HOMEIMPROVEMENT", "Home Improvement"), ("MEDICAL", "Medical"), ("PERSONAL", "Personal"), ("VENTRUE", "Venture"))
    home_ownership_choices = (("MORTGAGE", "Mortgage"), ("OTHER", "Other"), ("OWN", "Own"), ("RENT", "Rent"))
    
    # Create form values
    account_number = forms.IntegerField()
    credit_history_length = forms.IntegerField()
    historical_defaults = forms.IntegerField()
    loan_amount = forms.IntegerField()
    loan_grade = forms.ChoiceField(choices=loan_grade_choices)
    loan_interest_rate = forms.IntegerField()
    loan_intent = forms.ChoiceField(choices=loan_intent_choices)
    loan_percent_income = forms.IntegerField()
    person_age = forms.IntegerField()
    person_employment_length = forms.IntegerField()
    person_home_ownership = forms.ChoiceField(choices=home_ownership_choices)
    person_income = forms.IntegerField()