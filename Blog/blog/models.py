from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 20)
    author = models.CharField(max_length = 10)
    category = models.CharField(max_length = 20)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    allow_comments = models.BooleanField()

    def __str__(self):
        return "[" + self.category + "] " + self.title