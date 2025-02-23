from django.db import models

class ExtractedText(models.Model):
    content = models.TextField()  # Stores extracted text
    file_type = models.CharField(max_length=10)  # Indicates PDF or Image
    uploaded_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when text was extracted

    def __str__(self):
        return f"{self.file_type} - {self.uploaded_at}"
