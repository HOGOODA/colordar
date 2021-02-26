from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# day as td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(create_date__day=day)
		d = ''
		for event in events_per_day:
			# d += f'<li> {event.title} </li>'
			d += f'<li class="list"> {event.get_html_url} </li>'

		if day != 0:
			return f"<td><span class='date' id={day}>{day}</span><ul class={day}> {d} </ul></td>"
		return '<td></td>'

	# week as tr 
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# month as table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(create_date__year=self.year, create_date__month=self.month)

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal