from rest_framework import routers
from CashProject import views as myapp_views


router = routers.DefaultRouter()
router.register('users', myapp_views.UserProfileViewSet)
router.register('transaction', myapp_views.TransactionViewSet)
