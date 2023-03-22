from django.db import models

# Create your models here.

class employee_data(models.Model):
    Emp_id = models.IntegerField()
    Emp_name = models.CharField(max_length=20)
    date = models.DateField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    

    def __str__(self):
        return self.Emp_name