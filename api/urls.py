from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import MovieViewSet, RatingViewSet, UserViewSet # Correctly importing the views

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)  # Use the imported classes directly
router.register('ratings', RatingViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
