from rest_framework import routers
from django.urls import path, include

from staff.views import CarViewSet, VisitorViewSet, StaffViewSet, ReportViewSet
from staff.views.visitor_views import create_visitor
from staff.views.login_view import LoginView
from staff.views.logout_view import LogoutView
router = routers.DefaultRouter(trailing_slash=False)

router.register(r'car', CarViewSet)
router.register(r'visitor', VisitorViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'report', ReportViewSet)

urlpatterns = [
     path('login/', LoginView.as_view()),
     path('create_visitor/', create_visitor),
     path('logout/', LogoutView.as_view()),
]

urlpatterns += router.urls
