from django.db import models
import uuid




class Submissions(models.Model):
    file_name = models.CharField(max_length=200, default="")
    file_type = models.CharField(max_length=200)
    backend_qa_results = models.JSONField(default=dict)
    guid = models.UUIDField(default=uuid.uuid4())
    isp_name = models.CharField(max_length=200, default="")


