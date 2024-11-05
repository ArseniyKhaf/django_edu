from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Model for goods category."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
        max_length=100,
    )

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Goods(models.Model):
    """Model for goods"""

    name = models.CharField(
        max_length=150,
        verbose_name="Название",
    )
    category = models.ManyToManyField(
        Category,
        related_name="goods",
        verbose_name="Категории",
        null=True,
        blank=True,
    )
    description = models.TextField(
        max_length=500,
        verbose_name="Описание",
        null=True,
        blank=True,
    )
    prise = models.FloatField(
        verbose_name="Цена в руб.",
        help_text="Можно использовать нецелые числа."
    )
    image = models.ImageField(
        verbose_name="Цена",
        upload_to="img/%Y/%m/%d/", #Фото(год, месяц, день)
    )
    adding_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
        max_length=100,
    )

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class CategoryFeedback(models.Model):
    """Model for feedback category."""

    name = models.CharField(
        max_length=100,
        verbose_name="Название",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
        max_length=100,
    )

    def __str__(self) -> models.CharField:
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Feedback(models.Model):
    """Model for goods feedback."""

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
    )

    text = models.CharField(
        max_length=150,
        verbose_name="Текст",
    )
    category = models.ManyToManyField(
        CategoryFeedback,
        related_name="feedback",
        verbose_name="Категории",
        null=True,
        blank=True,
    )

    image = models.ImageField(
        verbose_name="Фото",
        upload_to="img/%Y/%m/%d/", #Фото(год, месяц, день)
    )
    adding_time = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(
        unique=True,
        verbose_name="Слаг",
        max_length=100,
    )

    def __str__(self) -> models.CharField:
        return self.text

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
