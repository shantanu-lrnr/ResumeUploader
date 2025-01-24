from django import forms
from .models import Resume

GENDER_CHOICES = [
    ('Male','Male'),
    ('Female','Female'),
]

JOB_CITY_CHOICE = [
 ('Delhi', 'Delhi'),
 ('Pune', 'Pune'),
 ('Ranchi', 'Ranchi'),
 ('Mumbai', 'Mumbai'),
 ('Dhanbad', 'Dhanbad'),
 ('Banglore', 'Banglore')
]



class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect())
    
    job_city = forms.MultipleChoiceField(choices=JOB_CITY_CHOICE,label='Preferred Job Location',widget=forms.CheckboxSelectMultiple())

    class Meta:

        model = Resume

        fields = '__all__'

        labels = {
            'name':'Full Name',
            'dob' : 'Date of Birth',
            'pin' : 'Pin Code',
            'mobile' : 'Mobile No.',
            'profile_img':'Profile Image',
            'my_file': 'Document',
            'email': 'Email ID',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','autofocus':True}),
            # 'dob': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            'dob': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
            'locality': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
        }