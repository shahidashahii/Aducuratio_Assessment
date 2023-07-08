from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        fields=['username','password']
        widgets={'password':forms.PasswordInput()}

        help_texts={'username':' '}

class LaptopForm(forms.ModelForm):
    class Meta():
        model =Laptops
        fields = '__all__'

        widgets={
            'LaptopName':forms.TextInput(attrs={'class':'form-control'}),
            'LaptopModel':forms.TextInput(attrs={'class':'form-control'}),
            'LapImage':forms.FileInput(attrs={'class':'form-control'}),
            'Price':forms.NumberInput(attrs={'class':'form-control'}),
            'RAM':forms.TextInput(attrs={'class':'form-control'}),
            'Description':forms.Textarea(attrs={'class':'form-control'})
            
        }
    