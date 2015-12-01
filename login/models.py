from datetime import datetime
from django.db import models
from django.utils import timezone
TITLE_CHOICES = (
    ('Datastructure', 'Datastructure'),
    ('WebProgramming', 'WebProgramming'),
    ('General', 'General'),
    ('Java', 'Java'),
    ('DBMS', 'DBMS')
)

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    subject = models.CharField(max_length=15, choices=TITLE_CHOICES)
    question = models.CharField(max_length=300)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.subject

