from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'Categories'


class Story(models.Model):
    author = models.CharField(max_length=100, default='', null=True)
    descendants = models.IntegerField(default=0, null=True)
    story_id = models.IntegerField(null=True)
    score = models.IntegerField(default=0, null=True)
    text = models.TextField(default='', null=True)
    time = models.IntegerField(default=0, null=True)
    title = models.CharField(max_length=100, default='', null=True)
    type = models.CharField(max_length=100, default='', null=True)
    category_name = models.CharField(max_length=100, default='')
    url = models.CharField(max_length=100, default='', null=True)
    category_id = models.ForeignKey(Category, default=0, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Stories'