from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Because we are using class based views, each class may provide one or more HTTP method functions (get() , post() , put() , patch()  etc...)
# .as_view() is provided by Django and returns a callable view which the URL can pass in the request object to be processed by the view.
# For Django class-based views we access an appropriate view function by calling the class method as_view().
# This does all the work of creating an instance of the class, and making sure that the right handler methods are called for incoming HTTP requests
# W praktyce, as_view() zwróci odpowiednią callable, w zależności czy mamy do czynenia z POST, GET czy innym requestem.

# With Viewsets we use Routers.
# Routers aren't designed for normal views. You need to use ViewSet if you want register you url to your router.
# Ja to rozumiem tak, że w APIView definiujemy metody POST, GET itd. w klasie, więc już sama klasa jest jakby naszym routerem. Definiujemy co robimy w razie konkretnych metod HTTP,
# i następnie przypisujemy tę klasę do urlpatterns. Z kolei w przypadku viewsets korzystamy tylko z technik obsługi REST API, takich jak create, delete itd, więc router sam za nas ogarnia
# jaka metoda będzie przypisana do jakiego requesta HTTP i następnie produkuje liste URLs które podpinamy do urlpatterns.
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello_viewset')  # With routers, we don't need to add slashes in the url, it will be handled for us automatically
# We don't need a basename, because we have a queryset declared in UserProfileViewSet, and Django will figure out the name from the Model assigned to this ViewSet
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)

# include() -> this is used for including list of URLs inte URL pattern and assigning the lists to a specific URL
urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('login/', views.UserLoginAPIView.as_view()),
    # When we register new routes in our router, it generates a list of URLs that are associated with our ViewSet.
    # It figures out the URLs that are required for all the functions that we add to our ViewSet, and then it generates the URLs list which we can pass in to the path using include.
    path('', include(router.urls))
]
