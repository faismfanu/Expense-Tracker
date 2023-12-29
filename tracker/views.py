from django.shortcuts import render
from .models import Expense
from rest_framework import generics
from .serializer import ExpenseSerializer

# Create your views here.

# Listing Expense View
class ExpenseListView(generics.ListAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

# Creating Expense View
class ExpenseCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer



