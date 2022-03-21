from rest_framework import routers

from gate.views import CameraViewSet, GateViewSet, HomeViewSet
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'camera', CameraViewSet, basename='camera')
router.register(r'gate', GateViewSet, basename='gate')
router.register(r'', HomeViewSet, basename='home')

urlpatterns = [

]

urlpatterns += router.urls
