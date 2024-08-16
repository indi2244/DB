from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
        return self.name
    
class Brand2(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
        return self.name
    
class Brand3(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
        return self.name
    
class Brand4(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
        return self.name

class Brand5(models.Model):
    name = models.CharField(max_length=100)
    founded = models.IntegerField()

    def __str__(self):
        return self.name