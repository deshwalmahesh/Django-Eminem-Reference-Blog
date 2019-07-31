from blog.models import Post,Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class PostForm(forms.ModelForm):

    class Meta:
        model= Post
        fields=('author','title','text')

        widgets={
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields=('author','text')

        widgets={
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class SignupForm(UserCreationForm):
    first_name=forms.CharField(label="First Name")
    # Use forms.TextArea for an address like box
    last_name=forms.CharField(label='Last Name')

    #Removes the help_texts
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = None

        '''def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None'''

    class Meta:
        model=User
        fields=('first_name','last_name','username','email','password1','password2')


