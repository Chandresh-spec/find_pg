from django  import  forms


class NameForm(forms.Form):
    username=forms.CharField(
        max_length=50,
        widget=forms.TextInput(attrs={'placeholder':'Enter your name'})
    )

class EmailForm(forms.Form):
    email=forms.EmailField(
        
        widget=forms.TextInput(attrs={'placeholder':'Enter your  Email'})
    )


class PhoneForm(forms.Form):
    phone=forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={'placeholder':'Enter your Phone Number'})
    )



class PasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'})
    )


class ProfilePitureForm(forms.Form):
    profile_piture=forms.ImageField(
        required=False,
        widget=forms.FileInput(attrs={'accept': 'image/*'})
    )



class BioForm(forms.Form):
    bio = forms.CharField(
        max_length=300,
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Tell us about yourself', 'rows': 3})
    )