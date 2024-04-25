from django.urls import path
from . import views




urlpatterns = [
    

    path('',views.list_expenses),
    path('expenses',views.list_expenses),
    path('expenses/<int:pk>/',views.detail_expense),
    path('categories',views.list_categories)

]


# expenses = http://127.0.0.1:8000/expenses
# categories = http://127.0.0.1:8000/categories
# del_expenses = http://127.0.0.1:8000/expenses/id