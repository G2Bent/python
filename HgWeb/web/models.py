from django.db import models
import time
import os
# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=30)
    # name = models.FileField(name="%Y%m%d%H%M%S")
    fileway = models.FileField(upload_to="hey/Heygears/Excel/%Y%m%d%H%M%S")
    uploadtime =models.DateTimeField("创建时间",auto_now_add=True)
    def __unicode__(self):
        return self.filename