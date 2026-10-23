from django.db import models

# Create your models here.
class Reza(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_done = models.BooleanField(default=False)
    created_at = models.DateTimeField()
    update_at = models.DateTimeField()

    def __str__(self):
        return f"{self.title} ----- {self.created_at}"