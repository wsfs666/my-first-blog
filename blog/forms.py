from django import forms
#导入Django表单

from .models import Post
#导入Post模型
class PostForm(forms.ModelForm):
    #PostForm 表单模型名字
    #

    class Meta:
        model = Post
        fields = ('title', 'text',)