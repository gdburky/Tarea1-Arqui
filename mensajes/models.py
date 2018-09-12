from django.db import models

class Messege(models.Model):
    messege = models.CharField(max_length=500)
    pub_date = models.CharField(max_length=100)
    client_ip = models.CharField(max_length=100)

    def __str__(self):
        return self.messege



