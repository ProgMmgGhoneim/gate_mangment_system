from django.contrib import admin

from staff.models.car import Car
from staff.models.staff import Staff
from staff.models.visitor import Visitor
from staff.models.visitor_trace import VisitorTrace
from staff.models.report import Report

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'visitor', 'plate_number', 'status', 'created_at', 'updated_at')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at')

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'job_title', 'reason_of_visit', 'created_at', 'updated_at')

admin.site.register(VisitorTrace)
admin.site.register(Report)
