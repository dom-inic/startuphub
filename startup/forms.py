from django.forms import forms
from . models import Startup
from django.forms.models import ModelForm

class NewStartupForm(ModelForm):
	class Meta:
		model = Startup
		exclude = ("date_added",'category', )
		field= ("name",  "funding", "funding_reason", "image", "description", "location", "address", "email", "phone_no", "website")
		# widget = {
		# 	"category" : forms.SelectInput(
		# 		attrs={
		# 		"required": True,
		# 		"class": "form-control",
		# 		}
		# 		)

		# }