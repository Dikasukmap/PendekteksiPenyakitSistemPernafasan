from django import forms
from appTB.models import User
from captcha.fields import CaptchaField

class NewUserForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = User
        widgets = {
        'username' : forms.TextInput(attrs={'placeholder': 'Username Account Anda'}),
        'nickname' : forms.TextInput(attrs={'placeholder': 'Tampilan Nama Anda dalam Game'}),
        'password': forms.PasswordInput(attrs={'placeholder': 'Password Account Anda'}),
        'retype_Password': forms.PasswordInput(attrs={'placeholder': 'Konfirmasi Password Account Anda'}),
        'email' : forms.TextInput(attrs={'placeholder': 'Email harus Valid dan Benar e.g email_anda@example.com'}),
        'no_Telepon' : forms.TextInput(attrs={'placeholder': 'Nomor Telepon Anda'}),
        }
        fields = '__all__'
