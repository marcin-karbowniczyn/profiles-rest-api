from django.urls import path
from . import views

# Because we are using class based views, each class may provide one or more HTTP method functions (get() , post() , put() , patch()  etc...)
# .as_view() is provided by Django and returns a callable view which the URL can pass in the request object to be processed by the view.
# For Django class-based views we access an appropriate view function by calling the class method as_view().
# This does all the work of creating an instance of the class, and making sure that the right handler methods are called for incoming HTTP requests
# W praktyce, as_view() zwróci odpowiednią callable, w zależności czy mamy do czynenia z POST, GET czy innym requestem.


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
]
