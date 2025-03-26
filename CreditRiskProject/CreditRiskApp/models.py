from django.db import models

# Create your models here.
class CreditRisk(models.Model):
    # Define choice fields
    loan_grade_choices = (("A","A"), ("B", "B"), ("C", "C"), ("D", "D"), ("E", "E"), ("F", "F"))
    loan_intent_choices = (("DEBTCONSOLIDATION", "Debt Consolidation"), ("EDUCATION", "Education"), ("HOMEIMPROVEMENT", "Home Improvement"), ("MEDICAL", "Medical"), ("PERSONAL", "Personal"), ("VENTRUE", "Venture"))
    home_ownership_choices = (("MORTGAGE", "Mortgage"), ("OTHER", "Other"), ("OWN", "Own"), ("RENT", "Rent"))
    
    # Create model values
    account_number = models.IntegerField()
    credit_history_length = models.IntegerField()
    historical_defaults = models.IntegerField()
    loan_amount = models.IntegerField()
    loan_grade = models.CharField(max_length=50, choices=loan_grade_choices)
    loan_interest_rate = models.FloatField()
    loan_intent = models.CharField(max_length=50, choices=loan_intent_choices)
    loan_percent_income = models.FloatField()
    person_age = models.IntegerField()
    person_employment_length = models.FloatField()
    person_home_ownership = models.CharField(max_length=50, choices=home_ownership_choices)
    person_income = models.IntegerField()
    will_default = models.CharField(max_length=50, default=None)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.account_number