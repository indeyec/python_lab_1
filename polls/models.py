import datetime
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from audioop import reverse
from django.db import models
from django.core.validators import RegexValidator


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class AdvUser(AbstractUser):
    middle_name = models.CharField('Отчество', max_length=50)
    last_name = models.CharField(max_length=12, verbose_name="Фамилия", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Фамилия введена не правильно',
                       code='invalid_last_name'), ])
    first_name = models.CharField(max_length=12, verbose_name="Имя", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Имя введено не правильно',
                       code='invalid_first_name'), ])
    middle_name = models.CharField(max_length=12, verbose_name="Отчество", validators=[
        RegexValidator(regex=r'[а-яА-ЯёЁ]+$', message='Отвество введено не правильно',
                       code='invalid_middle_name'), ])
    role = models.CharField(max_length=254, verbose_name='Роль',
                            choices=(('admin', 'Администратор'), ('user', 'Пользователь'), ('author', 'Автор')),
                            default='user')
    username = models.CharField(max_length=20, verbose_name="Имя пользователя", unique=True, validators=[
        RegexValidator(regex=r'^[a-z]+$', message='Имя пользователя введено не правильно',
                       code='invalid_username'), ])

    def delete(self, *args, **kwargs):
        for bb in self.bb_set.all():
            bb.delete()
        super().delete(*args, **kwargs)

    def is_author(self, bb):
        if self.pk == bb.author.pk:
            return True
        return False

    class Meta(AbstractUser.Meta):
        pass