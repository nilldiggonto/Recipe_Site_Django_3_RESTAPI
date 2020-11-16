from django import forms
from django.contrib.auth import authenticate,login,get_user_model,logout

User = get_user_model()


class UserLoginForm(forms.Form):
    username    = forms.CharField()
    password    = forms.CharField(widget=forms.PasswordInput)

    def clean(self,*args,**kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        user = authenticate(username=username, password= password)
        if not user:
            raise forms.ValidationError('Credentials is not matching')
        # if not user.check_password(password):
        #     raise forms.ValidationError('Password Wrong')
        if not user.is_active:
            raise forms.ValidationError('ID Blocked')
        return super(UserLoginForm,self).clean(*args,**kwargs)


class UserRegisterForm(forms.ModelForm):
    email2 =  forms.EmailField(label='Email')
    email2 =  forms.EmailField(label='Confirm Email')
    password    = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'email2',
            'password'
        ]

    def clean_email2(self):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Email not Matchin')

        email_qs = User.objects.filter(email= email)
        if email_qs.exists():
            raise forms.ValidationError('Email Already Exists')
        return email