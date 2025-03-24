from django.shortcuts import render
from .forms import CreditRiskForm
from .models import CreditRisk
import pandas as pd
import os
from django.conf import settings
import joblib
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import CreditRiskSerializer

class CreditRiskListCreate(generics.ListCreateAPIView):
    queryset = CreditRisk.objects.all()
    serializer_class = CreditRiskSerializer
    
    def delete(self, request, *args, **kwargs):
        CreditRisk.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CreditRiskRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    model = CreditRisk
    serializer_class = CreditRiskSerializer
    lookup_field = "pk"

def oneHotEncode(df:pd.DataFrame):
    # Define path to feature columns
    features_path = os.path.join(settings.BASE_DIR, "CreditRiskApp", "resources", "ohe_cols.pkl")
    
    features = joblib.load(features_path)  # Dataset features
    df_processed = pd.get_dummies(df, drop_first=False)  # One Hot Encode the data
    
    new_dict = dict()
    for col in features:
        if col in df_processed.columns:
            new_dict[col] = df_processed[col].values  # Store column and its values to dictionary
        else:
            new_dict[col] = 0  # Assign zero to column value
            
    # Create new DataFrame
    new_df = pd.DataFrame(new_dict, index=[0])
    new_df.replace({True:1, False:0})
    
    return new_df

def predict(df:pd.DataFrame):
    # Load the model
    model_path = os.path.join(settings.BASE_DIR, "CreditRiskApp", "resources", "model.pkl")
    model = joblib.load(model_path)
    
    y_pred = model.predict(df)  # Predict Credit Risk
    
    return y_pred

def form(request):
    if request == "POST":
        form = CreditRiskForm(request.POST)  # Define the form
        if form.is_valid():
            # Initialize form fields
            account_number = form.cleaned_data["account_number"]
            credit_history_length = form.cleaned_data["credit_history_length"]
            historical_defaults = form.cleaned_data["historical_defaults"]
            loan_amount = form.cleaned_data["loan_amount"]
            loan_grade = form.cleaned_data["loan_grade"]
            loan_interest_rate = form.cleaned_data["loan_interest_rate"]
            loan_intent = form.cleaned_data["loan_intent"]
            loan_percent_income = form.cleaned_data["loan_percent_income"]
            person_age = form.cleaned_data["person_age"]
            person_employment_length = form.cleaned_data["person_employment_length"]
            person_home_ownership = form.cleaned_data["person_home_ownership"]
            person_income = form.cleaned_data["person_income"]
            
            new_dict = (request.POST).dict()  # Create new dictionary
            new_df = pd.DataFrame(new_dict, index=[0])  # Create new DataFrame
            new_df.drop("account_number", axis=1, inplace=True)  # Drop columns that are not used in the model
            
            result = predict(oneHotEncode(new_df))  # Get classification Reslts
            
            CreditRisk.objects.create(
                account_number = account_number,
                credit_history_length = credit_history_length,
                historical_defaults = historical_defaults,
                loan_amount = loan_amount,
                loan_grade = loan_grade,
                loan_interest_rate = loan_interest_rate,
                loan_intent = loan_intent,
                loan_percent_income = loan_percent_income,
                person_age = person_age,
                person_employment_length = person_employment_length,
                person_home_ownership = person_home_ownership,
                person_income = person_income,
                will_default = result
            )
            
            render(request, "result.html", {"result":result})  # Redirect to the result page
            
        form = CreditRiskForm()
        
    render(request, "index.html", {"form":form})