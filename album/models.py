from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
# Create your models here.
class albumModel(models.Model):
    public='public'
    private='private'
    author=models.ForeignKey(User,on_delete= models.CASCADE)
    access={
        public:'pub',
        private:'pvt'
    }
    Title=models.CharField(max_length=10)
    albumaccess=models.CharField(max_length=10,choices=access,default=private)
    def get_post(self,Post):
        return Post.objects.filter(Q(album=self))
    def __str__(self):
        return self.Title