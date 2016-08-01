from __future__ import unicode_literals
from django.db import models
from datetime import date

from .choices import POC_Status
from .choices import POC_Countries
from .choices import POC_location
from .choices import POC_Primary_Catagory
from .choices import POC_Gss_Services_required



# Create your models here.
class poc_request(models.Model):
	insight_quote = models.IntegerField(unique=True, verbose_name='Primary insight quote')
	insight_quote_add = models.TextField(blank=True, null=True, verbose_name='Additional insight quotes')
	customer_name = models.CharField(max_length=120)
	country = models.CharField(max_length=2, choices=POC_Countries)
	deal_value = models.IntegerField(verbose_name='estimated deal value $')
	poc_request_date = models.DateField(default=date.today)
	poc_status = models.CharField(max_length=12, choices=POC_Status, default='OPEN')
	poc_order_number = models.IntegerField(blank=True, null=True)
	requester_name = models.CharField(max_length=35)
	requester_email = models.EmailField()
	requester_number = models.CharField(max_length=14, verbose_name='requester mobile number')
	approval_manager_name = models.CharField(max_length=35)
	approval_manager_email = models.EmailField()
	presales_name = models.CharField(max_length=35)
	presales_email = models.EmailField()
	tech_sol_sup = models.CharField(max_length=3, verbose_name='Technical solution support', choices=POC_Gss_Services_required)
	poc_start_date = models.DateField()
	poc_end_date = models.DateField()
	poc_location = models.CharField(max_length=8, choices=POC_location)
	poc_pri_cat = models.CharField(max_length=15, verbose_name='Poc primary category', choices=POC_Primary_Catagory)
	poc_sec_cat = models.CharField(max_length=24)
	poc_testplan = models.FileField(upload_to='testplan/%Y-%m-%d', blank=True, null=True)
	poc_solution_design = models.FileField(upload_to='solution_design/%Y-%m-%d')
	poc_description = models.TextField()

	def __unicode__(self): ##python 3 use __str__
		return str(self.insight_quote)