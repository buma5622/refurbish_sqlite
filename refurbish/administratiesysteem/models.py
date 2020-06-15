from django.db import models

computer_type = (
    ('laptop', 'laptop'),
    ('desktop', 'desktop')
)


class Computer(models.Model):
    merk = models.TextField(max_length=50)
    type = models.CharField(choices=computer_type, max_length=50)
    processor = models.TextField(max_length=50)
    werkgeheugen =models.TextField(max_length=50)
    defecten = models.TextField(max_length=50)
    afbeelding = models.ImageField(blank=True, null=True)
    gerepareerd = models.BooleanField(default=False)

    def __str__(self):
        return self.merk

