from django.db import models

class repairRequest(models.Model):
    author = models.CharField('ФИО', max_length=45)
    contacts = models.IntegerField('Телефон')
    brandCar = models.CharField('Марка автомобиля', max_length=45)
    date = models.DateTimeField(auto_now_add=True, editable=True, null=True)
    problem = models.TextField('Проблема')
    MY_CHOICES = (
        ("1", 'Обработка'),
        ("2", 'В ремонте'),
        ("3", 'Выполнено'),
    )
    status = models.CharField(max_length=3, choices=MY_CHOICES, default=1)

