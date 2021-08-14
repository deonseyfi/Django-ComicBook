from django import forms
from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserChangeForm

from comicsite.models import User, Follow, Post
from comicsite.models import UserProfile, FavoriteComics
from comicsite.models import Comment, Rating


class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Username'
        }
    ))

    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'First name'
        }
    ))

    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Last name'
        }
    ))

    email = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Email'
        }
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Password'
        }
    ))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    usercity = forms.CharField(required=False)
    profpic = forms.ImageField(required=False)

    usercity = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'City'
        }
    ))

    class Meta:
        model = UserProfile
        fields = ('usercity', 'profpic')


class CommentForm(forms.ModelForm):
    text = forms.CharField(max_length=128)
    text = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'enter your comment here',
        }
    ))

    class Meta:
        model = Comment
        fields = ('text',)


'''
class PostRatingForm(forms.ModelForm):
    post_rating = models.BooleanField(null=True)

    class Meta:
        model = PostRating
        fields = ('post rating',)
'''


class RatingForm(forms.ModelForm):
    rating = forms.IntegerField(max_value=5, min_value=0)

    class Meta:
        model = Rating
        fields = ('rating',)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Wrong username or password. Try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class PostForm(forms.ModelForm):
    title = forms.CharField(required=True)
    title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': "form-control",
            'placeholder': 'Title'
        }
    ))

    text = forms.CharField(required=False)
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': "form-control2",
            'placeholder': 'Body',
        }
    ))

    image = forms.ImageField(required=False)

    class Meta:
        model = Post
        exclude = ["user"]
        fields = ('title', 'text', 'image')


class FavComicForm(forms.ModelForm):
    class Meta:
        model = FavoriteComics
        exclude = ["userid", "comicid"]


class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        exclude = ["user", "following"]


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {'first_name', 'last_name', 'email', 'username', 'password'}


class UploadPhotoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('profpic',)
