from django.db import models

class EmpInsert(models.Model):
    empname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    class Meta:
        db_table = "newemployeetable"