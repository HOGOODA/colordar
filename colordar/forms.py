from django.forms import ModelForm, DateInput
from colordar.models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event

    fields = '__all__'

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    

