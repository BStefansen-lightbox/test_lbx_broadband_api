from django.db import models


class Submissions(models.Model):
    file_type = models.CharField(max_length=200)

