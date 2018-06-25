from django.db import models
from user.models import User
from django.urls import reverse


class Publication(models.Model):
    title = models.CharField(max_length=250)
    publisher_name = models.CharField(max_length=30)
    editorial_name = models.CharField(max_length=19)
    year = models.IntegerField()
    volume = models.PositiveSmallIntegerField()
    doi = models.CharField(max_length=128, verbose_name='DOI', blank=True)
    isbn = models.CharField(max_length=32, verbose_name="ISBN", null=True,	help_text='13 character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    description = models.TextField()
    edition = models.FloatField()
    language = models.CharField(max_length=10)
    pages = models.IntegerField()
    date_of_addition = models.DateTimeField()
    abstract = models.TextField()
    featured = models.BooleanField(default=False, help_text='Hide publications from main view.')
    type = models.CharField(max_length=10, help_text='Type of publication')


    def get_absolute_url(self):
        return reverse('publications:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.publisher_name + ',' + self.editorial_name + ',' + self.year + ','  +  self.title



class PublicationAuthor(models.Model):
    publication_id = models.ForeignKey(Publication, on_delete=None)
    author = models.ForeignKey(User, on_delete=None)


class NewsletterSubmission(models.Model):
    author = models.ForeignKey(User, on_delete=None)
    text = models.TextField()
    attachment = models.FileField()
    date = models.DateTimeField()
    edition = models.PositiveSmallIntegerField()


class NewsletterPublished(models.Model):
    editor = models.ForeignKey(User, on_delete=None)
    edition = models.PositiveSmallIntegerField()
    date = models.DateTimeField()
    attachment = models.FileField()
    text = models.TextField()


