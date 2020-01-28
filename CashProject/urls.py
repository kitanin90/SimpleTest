from django.urls import include, path
from rest_framework import routers
from CashProject import views

router = routers.DefaultRouter()
router.register('usersprofile', views.UserProfileViewSet)
router.register('transactions', views.TransactionViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
