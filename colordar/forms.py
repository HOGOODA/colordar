from django.forms import ModelForm, DateInput, HiddenInput
from colordar.models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    fields = ['title','description']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    

