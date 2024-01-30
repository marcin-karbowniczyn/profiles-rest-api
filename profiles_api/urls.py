from django.urls import path
from . import views

# Because we are using class based views, each class may provide one or more HTTP method functions (get() , post() , put() , patch()  etc...)
# .as_view() is provided by Django and returns a callable view which the URL can pass in the request object to be processed by the view.

urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
]
