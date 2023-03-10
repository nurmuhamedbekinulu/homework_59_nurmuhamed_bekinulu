from django.db import models


class Project(models.Model):
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        verbose_name="Название"
    )
    description = models.TextField(
        max_length=3000,
        null=False,
        blank=False,
        verbose_name="Описание"
    )
    start_date = models.DateField(
        null=False,
        blank=False,
        verbose_name="Дата начала"
    )
    completion_date = models.DateField(
        null=True,
        blank=True,
        verbose_name="Дата окончания"
    )

    def __str__(self):
        return self.title
