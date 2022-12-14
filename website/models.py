from django.db import models
from django.contrib.auth.models import User


class MyApp(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to='my_apps')
    url = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='my_apps')

    def __str__(self):
        return f'MyApp {self.id}: {self.name}'

    class Meta:
        verbose_name_plural = 'my apps'
        ordering = ['name']
