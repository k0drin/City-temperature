from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class CityTemperature(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='temperatures')
    value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city.name}: {self.value}°C at {self.created_at}"