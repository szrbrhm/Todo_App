from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=40)
    complete = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_date',)
    
    def __str__(self):
        return self.title
