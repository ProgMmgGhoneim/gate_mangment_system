from rest_framework import routers

from gate.views import CameraViewSet, GateViewSet
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'camera', CameraViewSet)
router.register(r'gate', GateViewSet)

urlpatterns = [

]

urlpatterns += router.urls
