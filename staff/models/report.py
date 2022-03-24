import os

from django.db import models
from django.core.files.base import ContentFile

from gate.base_model import BaseModel


class Report(BaseModel):
    name = models.CharField(max_length=200, blank=False, null=False)
    file = models.FileField(upload_to='reports/')

    def __str__(self):
        return self.name

    @staticmethod
    def get_or_create_file_path(filename, directory='reports'):
        path = directory + '/' + filename
        if not os.path.exists(directory):
            os.makedirs(directory)
        return path

    @classmethod
    def create_report_object(cls, filename, path):
        try:
            with open(path, 'rb') as buffer:
                with ContentFile(buffer.read()) as file_content:
                    report = cls.objects.create(name=filename)
                    report.file.save(path, file_content)
            return report
        except Exception as e:
            return None