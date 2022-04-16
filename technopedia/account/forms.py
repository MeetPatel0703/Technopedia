from django import forms
from .models import TechUser
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UserForm(UserCreationForm):
    class Meta():
        model = TechUser
        fields = ('username', 'email', 'password1', 'password2')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class Loginform(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'autofocus': True, 'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'current-password', 'class': 'form-control', 'placeholder': 'Password'}),
    )


# class UserForm(forms.ModelForm):
#     # password1 = forms.CharField(
#     #     widget=forms.PasswordInput(
#     #         attrs={'class': "form-control", 'placeholder': 'Password'}),
#     # )
#     # password2 = forms.CharField(
#     #     widget=forms.PasswordInput(
#     #         attrs={'class': "form-control", 'placeholder': 'Confirm Password'}),
#     #     help_text=_("Enter the same password as before, for verification."),
#     # )

#     password = forms.PasswordInput(
#         # widget=forms.PasswordInput(
#         #     attrs={'autocomplete': 'new-password', 'class': "form-control", 'placeholder': 'Password'}),
#     )

#     class Meta:
#         model = User
#         fields = ("username", "email", "password")
#         widgets = {'username': forms.TextInput(
#             attrs={'class': 'form-control', 'placeholder': 'Name'}),
#             'email': forms.EmailInput(
#             attrs={'class': 'form-control', 'placeholder': 'Email'})}  # ,
#     # 'password1': forms.PasswordInput(
    # attrs={'class': 'form-control', 'placeholder': 'Password', 'id': 'password'}),
    # 'password2': forms.PasswordInput(
    # attrs={'class': 'form-control', 'placeholder': 'cPassword', 'id': 'cpassword'})}
