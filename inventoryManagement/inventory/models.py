from django.db import models


class Laptop(models.Model):
    type = models.CharField(max_length=200, blank=False)
    data = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)


class Desktop(models.Model):
    type = models.CharField(max_length=200, blank=False)
    data = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)


class Mobile(models.Model):
    type = models.CharField(max_length=200, blank=False)
    data = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)


""""
class Device(models.Model):
    type = models.CharField(max_length=200, blank=False)
    data = models.CharField(max_length=200, blank=False)
    price = models.IntegerField()

    choices = (
        ('AVAILABLE', 'Item ready to be purchased'),
        ('SOLD', 'Item already purchased'),
        ('RESTOCKING', 'Item restocking in few days')
    )

    status = models.CharField(max_length=10, choices=choices, default='SOLD')
    issues = models.CharField(max_length=50, default="No Issues")

    class Meta:
        abstract = True

    def __str__(self):
        return 'Type: {0} Price: {1}'.format(self.type, self.price)


class Desktop(Device):
    pass


class Laptop(Device):
    pass


class Mobile(Device):
    pass
"""""
