from django.forms import ModelForm
from .models import Rent

class RentForm(ModelForm):
	class Meta:
		model = Rent
		fields = '__all__'