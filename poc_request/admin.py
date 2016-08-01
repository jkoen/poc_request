from django.contrib import admin

# Register your models here.
from .models import poc_request
from .forms import POC_RequestFormAdmin


# Customize admin look and feel
class POC_RequestAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "customer_name", "country", "deal_value", "poc_status"]
	form = POC_RequestFormAdmin
	# class Meta:
	# 	model = poc_request

admin.site.register(poc_request, POC_RequestAdmin)