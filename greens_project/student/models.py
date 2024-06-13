from django.db import models

# Create your models here.
class TestModel(models.Model):
    name = models.CharField(max_length=100)

# from myapp.models import TestModel
# TestModel.objects.create(name='Test Name')
# print(TestModel.objects.all())


# from django.db import connection
# try:
#     connection.ensure_connection()
#     print("Connection to MySQL is successful")
# except Exception as e:
    # print(f"Connection failed: {e}")