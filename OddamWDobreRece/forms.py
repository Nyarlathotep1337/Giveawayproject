from django import forms
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User

from OddamWDobreRece.models import Donation


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               validators=[validate_password],
                               help_text='Hasło ma być dłuższe niż 8')
    password2 = forms.CharField(label='re-Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['last_name', 'email']
        widgets = {
            # 'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-group'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'password', 'class': 'form-group'}),
                               required=False)

class DonationForm(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'

class DonationFormStep1(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['categories']

class DonationFormStep2(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['quantity']

class DonationFormStep3(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['institution']

class DonationFormStep4(forms.ModelForm):
    class Meta:
        model = Donation
        fields = ['address', 'city', 'zip_code', 'phone_number', 'pick_up_date', 'pick_up_time', 'pick_up_comment']

class DonationFormStep5(forms.ModelForm):
    class Meta:
        model = Donation
        fields = '__all__'