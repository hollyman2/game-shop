from django.db import models
from django.urls import reverse


class DefaultCategoryOrTagClass(models.Model):
    name = models.CharField(max_length=100)
    slug = name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Tag(DefaultCategoryOrTagClass):

    class Meta:
        db_table = 'Tag'


class Category(DefaultCategoryOrTagClass):

    class Meta:
        db_table = 'Category'


class Product(models.Model):
    # game = models.FileField(upload_to='')
    name = models.CharField(max_length=100)  # название
    tags = models.ManyToManyField(to=Tag)  # список тегов
    price = models.IntegerField()  # цена
    is_released = models.BooleanField()  # выпущена ли в продажу

    def __str__(self):
        return self.name


class Description(models.Model):
    game = models.ForeignKey(Product, on_delete=models.CASCADE)  # связь с игрой
    author = models.CharField(max_length=100)  # автор
    link_of_author = models.URLField()  # ссылка на автора
    release_date = models.DateField()  # дата выпуска
    date_of_update = models.DateField()  # дата обновления
    description = models.TextField()  # описание игры

    def __str__(self):
        return 'description' + '|' + self.game.name
