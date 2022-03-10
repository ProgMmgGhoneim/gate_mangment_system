from rest_framework import routers

from staff.views import CarViewSet, VisitorViewSet, StaffViewSet, ReportViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'car', CarViewSet)
router.register(r'visitor', VisitorViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'report', ReportViewSet)

urlpatterns = [

]

urlpatterns += router.urls
