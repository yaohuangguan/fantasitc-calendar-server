from rest_framework import routers
from .api import UserViewSet
from . import views

router = routers.DefaultRouter()
router.register('user', UserViewSet, 'appsource')

# router.register('/', views.homePageRsp)


urlpatterns = router.urls