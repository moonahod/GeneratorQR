from django.db import models

class Draft(models.Model):

    def __str__(self):
        return self.name
