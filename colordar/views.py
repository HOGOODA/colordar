from datetime import datetime, date
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils.safestring import mark_safe
from datetime import timedelta
from django.urls import reverse
import json
from .models import *
from .utils import Calendar
import calendar
from .forms import EventForm
from .predict_DL import predict_emotion
# from soynlp.tokenizer import LTokenizer
# from tensorflow.keras.preprocessing.text import Tokenizer
import numpy as np
import pickle 
import gzip
from django.conf import settings

diary=''

def index(request):
    return HttpResponse('hello')

# def event_data(request):
#     events=Event.objects.all()
#     context={
#         "events": events,
#         "events_js":json.dumps([event.json() for event in events])
#     }
#     return render(request, "")

class CalendarView(generic.ListView):
    model = Event
    template_name = 'colordar/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        get_month = get_date(self.request.GET.get('month', None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(get_month.year, get_month.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(get_month)
        context['next_month'] = next_month(get_month)
        calculate_day=datetime.today()
        context['result']=calculate_day.day
        context['today_color']= get_color()
        
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def prev_month(month_info):
    first = month_info.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(month_info):
    days_in_month = calendar.monthrange(month_info.year, month_info.month)[1]
    last = month_info.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month


def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        print(form.cleaned_data)
        diary=form.cleaned_data['description']
        post=form.save(commit=False)
        post.analyzed=get_predict(diary)
        post.save()
        print(post)

        return HttpResponseRedirect(reverse('colordar:calendar'))
    return render(request, 'colordar/event.html', {'form': form})


def get_predict(diary):
    if diary=='':
        return 9
    else:
        # base_url = settings.MEDIA_ROOT_URL + settings.MEDIA_URL
        # pickle_url = base_url + 'testPickleFile.pickle'
        # with gzip.open(pickle_url,'rb') as f:
        #     data = pickle.load(f)
        # scores = {word:score.cohesion_forward for word, score in data.items()}
        # l_tokenizer = LTokenizer(scores=scores)

        # tokenized_diary= l_tokenizer.tokenize(diary)
        # return tokenized_diary

        # vocab_size=len(tokenized_diary)
        # print(vocab_size)
        # tokenizer = Tokenizer(vocab_size, oov_token = 'OOV')
        # tokenizer.fit_on_texts(tokenized_diary)
        # tokenized_number= tokenizer.texts_to_sequences(tokenized_diary)
        # tokenized_np= np.asarray(tokenized_number).astype('float32')

        return predict_emotion(diary)


def get_color():
    try:
        return Event.objects.get(create_date=date.today()).analyzed
    except:
        return 9