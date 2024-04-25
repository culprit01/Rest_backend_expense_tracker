from django.shortcuts import get_object_or_404, render
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# Create your views here.




@api_view(["GET", "POST"])

def list_expenses(request):
    if request.method == "GET":
        expenses = Expense.objects.all()
        serializer = ExpenseSerializer(expenses,many = True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = ExpenseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


@api_view(["GET", "DELETE"])
def detail_expense(request, pk):
    expense = get_object_or_404(Expense,id=pk)
    if request.method == "GET":
        serializer = ExpenseSerializer(expense)
        return Response(serializer.data)
    
    elif request.method == "DELETE":
        expense.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(["GET"])
def list_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many = True)
    return Response(serializer.data)