from django import forms
from .models import Post ,Comment

class PostForm(forms.ModelForm):
    class Meta:
        model =Post
        exclude =('author',)

class CommentForm(forms.ModelForm):
    class Meta:
        model =Comment
        fields =['comment']
        error_messages = {
                    'comment': {
                        'required': "",  # Setting an empty string to remove the default message
                    },
                }

CHOISES=[
    ('Ascending',"Ascending"),
    ("Deascending","Deascending")
]
class ArrangeForm(forms.Form):
    arrange = forms.ChoiceField(choices=CHOISES)
