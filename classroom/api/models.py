from django.db import models


class Class(models.Model):
    name = models.CharField(max_length=15)
    year = models.IntegerField()
    students = models.ForeignKey('Students', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Classes'
        verbose_name = 'Class'


class Students(models.Model):
    MARK_CHOICES = [
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    ]
    fio = models.CharField(max_length=20)
    age = models.IntegerField()
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    mark = models.CharField(max_length=1, choices=MARK_CHOICES)

    def __str__(self):
        return self.fio

    class Meta:
        verbose_name_plural = 'Students'
        verbose_name = 'Student'


class Subject(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Subjects'
        verbose_name = 'Subject'
