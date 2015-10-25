#__author__ = 'lenovo'
from django import forms
from blog.models import MyBlog, Tag
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify



class BlogCreateForm(forms.ModelForm):
    tags = forms.CharField(help_text='Add tags separating by comma(,).')

    class Meta:
        model = MyBlog
        fields = ['title', 'body']
        widgets = {
            'body': forms.Textarea,
        }
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if(slugify(title)):
            return title
        raise forms.ValidationError("Enter The Title")

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag

        widgets = {
            'dwscription': forms.Textarea(),
        }

# class RegistrationForm(UserCreationForm):
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data["password"])
#         user.is_staff = False
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = user
#         field = ("username", 'first_name','last-name', 'email',)
# class LogoutForm(forms.Form):
#     def logout(self, request):
#         logout(request)
#         return True
# class LoginForm(forms.Form):
#     username =
#

