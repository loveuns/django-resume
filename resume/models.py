from django.db import models
from tagging.fields import TagField


class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    # photo = models.ImageField(upload_to='portfolio-img/%Y/%m/%d', blank=False, default='portfolio-img/no_image.png')
    photo = models.ImageField(upload_to='portfolio-img', blank=True, null=True)
    githublink = models.URLField('Github URL', blank=True, null=True)
    servicelink = models.URLField('Service URL', blank=True, null=True)
    tag = TagField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " - " + self.created.strftime("%Y-%m-%d %H:%M") + " - " + self.photo.url
