from django.contrib import admin

from .models import Emp

class AdminEmp(admin.ModelAdmin):
    list_display = ['empid','empname','salary']

admin.site.register(Emp,AdminEmp)
