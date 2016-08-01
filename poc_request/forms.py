from django.contrib.admin import widgets
from django import forms
from datetime import date
from datetime import timedelta

from .models import poc_request
from .choices import POC_Status
from .choices import POC_Countries
from .choices import POC_location
from .choices import POC_Primary_Catagory
from .choices import POC_Gss_Services_required

class POC_RequestForm(forms.ModelForm):
	class Meta:
		model = poc_request
		fields = [ 'insight_quote', 'insight_quote_add', 'customer_name', 'country', 'deal_value', 'requester_name', 'requester_email', 'requester_number', 'approval_manager_name','approval_manager_email', 'presales_name', 'presales_email', 'tech_sol_sup', 'poc_start_date', 'poc_end_date', 'poc_location', 'poc_pri_cat', 'poc_testplan', 'poc_solution_design', 'poc_description' ]


	def __init__(self, *args, **kwargs):
    		super(POC_RequestForm, self).__init__(*args, **kwargs)
        	self.fields['insight_quote'].widget = widgets.AdminIntegerFieldWidget(attrs={'placeholder': '10056543'}) 
        	self.fields['insight_quote_add'].widget = forms.Textarea(attrs={'placeholder': '10056544 -- Compute','rows': 3, 'cols': 30}) ## Can also pass css in attr as 'style': 'height: 3em'
        	self.fields['customer_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Customer Name'})
        	self.fields['deal_value'].widget = widgets.AdminIntegerFieldWidget(attrs={'placeholder': '1000000'})
        	self.fields['requester_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Your Name'})
        	self.fields['requester_email'].widget = widgets.AdminEmailInputWidget(attrs={'placeholder': 'yourname.surname@hds.com'})
        	self.fields['requester_number'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': '+31418657500'})
        	self.fields['approval_manager_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Approval manager name'})
        	self.fields['approval_manager_email'].widget = widgets.AdminEmailInputWidget(attrs={'placeholder': 'Approval manager email'})
        	self.fields['presales_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Presales name'})
        	self.fields['presales_email'].widget = widgets.AdminEmailInputWidget(attrs={'placeholder': 'Presales email'})
        	self.fields['poc_start_date'].widget = widgets.AdminDateWidget(attrs={'placeholder': 'YYYY-mm-dd'})
        	self.fields['poc_end_date'].widget = widgets.AdminDateWidget(attrs={'placeholder': 'YYYY-mm-dd'})
        	self.fields['poc_description'].widget = widgets.AdminTextareaWidget(attrs={'placeholder': 'Provide as much detail as possible to describe the POC setup, objectives and customer expectations'})


	def clean(self):
		deal = self.cleaned_data.get('deal_value')
		if deal < 0:
			raise forms.ValidationError("Deal value cannot be zero, please provide the correct insight quote deal value")
		return deal

	def clean_requester_email(self):
		email = self.cleaned_data.get('requester_email')
		email_base, email_provider = email.split('@')
		email_domain, email_extention = email_provider.split('.')
		if not email_domain == 'hds':
			raise forms.ValidationError("Please use a valid HDS email address")
		return email

	def clean_approval_manager_email(self):
		email = self.cleaned_data.get('approval_manager_email')
		email_base, email_provider = email.split('@')
		email_domain, email_extention = email_provider.split('.')
		if not email_domain == 'hds':
			raise forms.ValidationError("Please use a valid HDS email address")
		return email

	def clean_presales_name(self):
		app_name = self.cleaned_data.get('approval_manager_name')
		pre_name = self.cleaned_data.get('presales_name')
		if app_name == pre_name:
			raise forms.ValidationError("Presales are not allowed to approve a POC")
		return pre_name	

	def clean_presales_email(self):
		pre_email = self.cleaned_data.get('presales_email')
		app_email = self.cleaned_data.get('approval_manager_email')
		email_base, email_provider = pre_email.split('@')
		email_domain, email_extention = email_provider.split('.')
		if pre_email == app_email:
			raise forms.ValidationError("Presales email and Approval manager email are identical")
		elif not email_domain == 'hds':
			raise forms.ValidationError("Please use a valid HDS email address")
		return pre_email

	def clean_poc_start_date(self):
		start_date = self.cleaned_data.get('poc_start_date')
		if start_date < date.today()+timedelta(days=5):
			raise forms.ValidationError("A minimum of at least 5 days is required for a basic POC assembly and configuration, choose %s" %(date.today()+timedelta(days=5)))
		return start_date

	def clean_poc_end_date(self):
		start_date = self.cleaned_data.get('poc_start_date')
		end_date = self.cleaned_data.get('poc_end_date')
		if not start_date:
			raise forms.ValidationError("Please set POC start date")
		elif end_date < start_date:
			raise forms.ValidationError("POC end date cannot be less than POC start date")
		return end_date


class POC_RequestFormAdmin(forms.ModelForm):
	class Meta:
		model = poc_request
		fields = [ 'insight_quote', 'insight_quote_add', 'customer_name', 'country', 'poc_request_date', 'poc_status', 'poc_order_number', 'deal_value', 'requester_name', 'requester_email', 'requester_number', 'approval_manager_name','approval_manager_email', 'presales_name', 'presales_email', 'tech_sol_sup', 'poc_start_date', 'poc_end_date', 'poc_location', 'poc_pri_cat', 'poc_testplan', 'poc_solution_design', 'poc_description' ]


	def __init__(self, *args, **kwargs):
    		super(POC_RequestFormAdmin, self).__init__(*args, **kwargs)
        	self.fields['insight_quote'].widget = widgets.AdminIntegerFieldWidget(attrs={'placeholder': '10056543'}) 
        	self.fields['insight_quote_add'].widget = forms.Textarea(attrs={'placeholder': '10056544 -- Compute','rows': 3, 'cols': 30}) ## Can also pass css in attr as 'style': 'height: 3em'
        	self.fields['customer_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Customer Name'})
        	self.fields['deal_value'].widget = widgets.AdminIntegerFieldWidget(attrs={'placeholder': '1000000'})
        	self.fields['poc_request_date'].widget.attrs['readonly'] = True
        	self.fields['poc_order_number'].widget = widgets.AdminIntegerFieldWidget(attrs={'placeholder': '20206329'})
        	self.fields['requester_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Your Name'})
        	self.fields['requester_email'].widget = widgets.AdminEmailInputWidget(attrs={'placeholder': 'yourname.surname@hds.com'})
        	self.fields['requester_number'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': '+31418657500'})
        	self.fields['approval_manager_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Account manager name'})
        	self.fields['approval_manager_email'].widget = widgets.AdminEmailInputWidget(attrs={'placeholder': 'Account manager email'})
        	self.fields['presales_name'].widget = widgets.AdminTextInputWidget(attrs={'placeholder': 'Presales name'})
        	self.fields['presales_email'].widget = widgets.AdminEmailInputWidget(attrs={'placeholder': 'Presales email'})
        	self.fields['poc_start_date'].widget = widgets.AdminDateWidget(attrs={'placeholder': 'YYYY-mm-dd'})
        	self.fields['poc_end_date'].widget = widgets.AdminDateWidget(attrs={'placeholder': 'YYYY-mm-dd'})
        	self.fields['poc_description'].widget = widgets.AdminTextareaWidget(attrs={'placeholder': 'Provide as much detail as possible to describe the POC setup, objectives and customer expectations'})













