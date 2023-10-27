from django import forms

from instagram.models import Post

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ['message', 'is_public']

# form = PostForm(request.Post)
# if form.is_valid():
#     post = form.save(commit=False) #instance.save호출되지 않기 위해
#     post.author = request.user
#     post.id = request.META['REMOTE_ADDR']
#     post.save()

