from django.db import models
import pathlib
import logging
import uuid
# Create your models here.
log=logging.getLogger(__name__)
def image_file_upload_handler(instance,filepath):
   instance_id=instance.id
   if not instance_id :
       instance_id=-1
   filepath=pathlib.Path(filepath).resolve()
   fname=str(uuid.uuid1())
   ext=filepath.suffix
   return f"album/{fname}{ext}"

class Post(models.Model):
    Title=models.CharField(max_length=30,default='')
    description=models.TextField(default='')
    image=models.ImageField(upload_to=image_file_upload_handler,blank=True,null=True)

    def get_data(self):
        data={
            'Title':self.Title,
            'description':self.description,
            'image':self.image
        }
        return data