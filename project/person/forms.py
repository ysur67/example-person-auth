from django import forms
from django.contrib.auth import authenticate


class LoginForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
            attrs = {
                'placeholder': "Логин"
            }),
        label="Ваш логин",
    )
    password = forms.CharField(
        widget = forms.PasswordInput(
            attrs = {
                'placeholder': 'Пароль'
            }
        ),
        label="Пароль"
    )
    
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username", None)
        password = cleaned_data.get("password", None)
        user = authenticate(username=username,
                            password=password)
        if not user:
            raise forms.ValidationError("Check the entered data")
        return cleaned_data
