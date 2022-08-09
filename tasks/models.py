from django.db import models

# Create your models here.
from django.utils.text import slugify


class Collection(models.Model):
    name = models.CharField(max_length=60)
    slug = models.SlugField()

    @classmethod
    def get_default_collection(cls) -> "Collection":
        collection, _ = Collection.objects.get_or_create(name="Défaut", slug="_defaut")
        return collection

    def __str__(self):
        return self.name

    #def save(self, *args, **kwargs):
       # self.slug = slugify(self.name)


class Task(models.Model):
    description = models.CharField(max_length=300)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.description
