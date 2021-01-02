from django.db import models
from .validators import validate_file_extension
from django.db import models
from django.utils import timezone

class upload(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    pdf = models.FileField(upload_to='document/pdfs/',validators=[validate_file_extension])

    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        self.cover.delete()
        super().delete(*args, **kwargs)
