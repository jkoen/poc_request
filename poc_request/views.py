from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib import messages 
from email.MIMEImage import MIMEImage
import os


from .forms import POC_RequestForm
from .models import poc_request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.
# For the contact form Try Django 1.8 Tutorial - 15 of 42

def send_email(to_list, subject, message, sender):
    msg = EmailMessage(subject, message, sender, to_list)
    msg.content_subtype = "html"  # Main content is now text/html
    fp = open(os.path.join(os.path.dirname(BASE_DIR), "static_env", "static_root", 'img/CoE.ico'), 'rb')
    msg_img = MIMEImage(fp.read())
    msg_img.add_header('Content-ID', '<{}>'.format('img/CoE.ico'))
    msg.attach(msg_img)
    return msg.send()


def home(request):
	if request.method == 'POST':
		form = POC_RequestForm(request.POST, request.FILES)
		title = "POC Request Form"
		context = {
				"title": title,
				"form": form,
		}
		
		if form.is_valid():
			#form.save() ## Save to DB immediatly 
			instance = form.save(commit=False) ## Allows us to do some stuff before saving
			# if not instance.presales_name:
			# 	instance.presales_name = "Not Provided"
			# if not instance.presales_email:
			# 	instance.presales_email = "Not Provided"
			instance.save()
			subject = 'POC Request for %s insight quote %i' %(instance.customer_name, instance.insight_quote)
			message = '''<p>Dear %s, </p>
						<p>
						The POC request for %s has been submitted. Please use the insight quote number %i as your reference number.<br> You will be contacted by the POC Team within the next 24 business hours.
						</p>
						Please familiarise yourself with the following content:
						<a href="http://loop.hds.com/community/saleshub/emea_spg/poc_request_emea/coe-poc-emea/frequently-asked-questions/overview"><strong>FAQ</strong></a>
						<a> & </a>
						<a href="http://loop.hds.com/community/saleshub/emea_spg/poc_request_emea/coe-poc-emea/center-of-excellence-guidelines"><strong>Guidelines</strong></a><br><br>
						Kind Regards<br>
						<strong>POC EMEA Team</strong><br>
						<img src="cid:img/CoE.ico">
						''' %(instance.requester_name, instance.customer_name, instance.insight_quote)
			sender = 'POC.Request.EMEA@hds.com'
			#to_list = [instance.requester_name, instance.approval_manager_email, from_email]
			to_list = ['johnny.koen@hds.com']
			#send_email(to_list, subject, message, sender)

			return HttpResponseRedirect('/thanks/')
	else:
		form = POC_RequestForm()
		title = "POC Request Form"
		context = {
				"title": title,
				"form": form,
		}
		

	return render(request, "home.html", context)
	# return render(request, "base.html", {})

def thanks(request):
	title = "POC Request Form"
	form = POC_RequestForm(request.POST or None)
	context = {
			"title": "Your request have been submitted and you will be contacted by the POC team within the next 24 business hours",
			"form": form,
		}
	return render(request, "thanks.html", context)

