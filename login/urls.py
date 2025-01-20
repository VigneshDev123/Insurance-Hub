
from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.home, name='home'),
    path('customer-login/', views.customer_login, name='customer_login'),
    path('agency-login/', views.agency_login, name='agency_login'),
    path('signup/', views.customer_signup, name='customer_signup'),
    path('main/', views.policy_list, name='Main'),
    path('purchase/<int:policy_id>/', views.purchase_policy, name='purchase_policy'),
    path('details/', views.user_details, name='user_details'),
    path('my_policies/', views.purchased_policies, name='purchased_policies'),
    path('file/<int:purchased_policy_id>/', views.file_claim, name='file_claim'),
]
