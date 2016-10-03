from django import forms



class DatabaseForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    CHOICES = [('select1','Male'),('select2','Female')]

    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
