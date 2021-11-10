from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    role = models.TextField()
    results = models.TextField()
    tech_stack = models.TextField()
    slug =  models.CharField(max_length=255)
    preview_image = models.CharField(max_length=255)
    images = models.CharField(max_length=255, null=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title