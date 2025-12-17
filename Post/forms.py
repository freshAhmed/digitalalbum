from .models import Post
from django.forms import ModelForm



class PostForm(ModelForm):
    class Meta:
        model=Post
        fields=['Title','description','image','album']

    def clean_Data(self):
    
     return self.clean() 

