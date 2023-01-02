from django.db import models

# Create your models here.

class masail(models.Model):
    Deskripsi = models.CharField(max_length=100)
    Jawaban = models.CharField(max_length=50)
    Tanggapan = models.CharField(max_length=50)
    keputusan = models.IntegerField(null=True)

    def __str__(self):
        return self.Asilah