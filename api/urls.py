from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'groups', views.GroupViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'members', views.MemberViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'profile', views.UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('authenticate/', views.CustomObtainAuthToken.as_view()),
]
