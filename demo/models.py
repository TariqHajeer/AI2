from django.db import models

# Create your models here.
class cityPath:
  def __init__(self, fromCity, toCity,value):
    self.fromCity = fromCity
    self.toCity = toCity
    self.value= value
