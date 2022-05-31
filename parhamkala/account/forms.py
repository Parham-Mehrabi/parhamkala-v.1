from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()
class registerform(forms.Form):
    error_css_class = 'text-danger'
    required_css_class = 'required'
    fname = forms.CharField(label='نام', required=True, max_length=64,
                            widget=forms.TextInput(attrs={'class': 'e-field-inner'}))
    last_name = forms.CharField(label='نام خانوادگی', required=True, max_length=64,
                                widget=forms.TextInput(attrs= {'class': 'e-field-inner'}))

    user_name = forms.CharField(label='نام کاربری', required=True, max_length=64,
                                widget=forms.TextInput(attrs={'class': 'e-field-inner'}))

    email = forms.EmailField(label='ایمیل', required=True, max_length=120,
                             widget=forms.EmailInput(attrs={'class': 'e-field-inner'}))

    passw = forms.CharField(label='رمز عبور', required=True, max_length=64,
                            widget=forms.PasswordInput(attrs={'class': 'e-field-inner'}))

    conf_passw = forms.CharField(label='تکرار رمز عبور', required=True, max_length=64,
                                 widget=forms.PasswordInput(attrs={'class': 'e-field-inner'}))

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("passw")
        password2 = self.cleaned_data.get("conf_passw")
        if password != password2:
            raise forms.ValidationError("پسورد ها یکی نیست")
        return data

    def clean_email(self):
        em = self.cleaned_data.get('email')
        e_mail = User.objects.filter(email=em)
        if e_mail.exists():
            raise forms.ValidationError('in email az ghabl vojood dare !!!')
        return em

    def clean_user_name(self):
        nimoone = self.cleaned_data.get('user_name')
        nemoone = User.objects.filter(username= nimoone)
        if len(nemoone):
            raise forms.ValidationError('in user name ghablan sabt shode !!!')
        return nimoone
