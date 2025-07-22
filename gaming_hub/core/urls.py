from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('games/', views.games_view, name='games'),
    path('contact/', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
]

from rest_framework.routers import DefaultRouter
from .api import GameViewSet

router = DefaultRouter()
router.register(r'api/games', GameViewSet)

urlpatterns += router.urls


from django.urls import path
from . import views


