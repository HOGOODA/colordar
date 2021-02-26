from django.db import models
from django.urls import reverse

class Event(models.Model):
    title = models.CharField(max_length=50,  verbose_name='제목')
    description = models.TextField(default='', verbose_name='내용')
    create_date = models.DateField(verbose_name='내용', auto_now_add=True)
    analyzed = models.CharField(max_length=3)

    @property
    def get_html_url(self):
        url = reverse('colordar:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'

    def __str__(self):
        return self.title


    def to_json(self):
        return{
            "title":self.title,
            "description":self.description,
            "create_date":self.create_date,
            "analyzed":self.analyzed
        }