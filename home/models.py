from django.db import models


class Dog(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title

class Cat(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title

class Fish(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title

class Hamster(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title


class Bird(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title


class Rabbit(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title

class Vip(models.Model):
    title =  models.CharField(max_length=255)
    img = models.ImageField(upload_to = 'Img')
    typ = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    price = models.FloatField()
    def __str__(self):
        return self.title

class Sargyt(models.Model):
    petname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.PositiveIntegerField()
    def __str__(self):
        return self.petname