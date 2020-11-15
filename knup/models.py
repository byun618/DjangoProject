from django.db import models

# Create your models here.
class File(models.Model):
    originalname = models.CharField(max_length=100)
    storedname = models.FileField(null=True, blank=True, upload_to="", max_length=200)
    userid = models.IntegerField()
    storeddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.storedname

    class Meta:
        ordering = ['storeddate']
        verbose_name = 'file'