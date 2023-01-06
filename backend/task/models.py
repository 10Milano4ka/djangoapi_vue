from django.db import models

# Create your models here.
class Task (models.Model):
    title = models.CharField(max_length=85)
    description = models.TextField(blank=True,null=True)
    comleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    

    def __str__(self) -> str:
        return self.title