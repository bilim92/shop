from django.urls import path

from applications.account.views import LoginApiView
from applications.product.views import ListCreateView, DeleteUpdateRetriveView

urlpatterns = [
    path('', ListCreateView.as_view()),
    path('<int:pk>/', DeleteUpdateRetriveView.as_view()),


]


