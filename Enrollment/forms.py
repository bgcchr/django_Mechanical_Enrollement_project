from django import forms
from . models import Enroll


class EnrollForm(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = [
            'Candidate_Name', 'Father_Name', 'Dob', 'Adress', 'city', 'state', 'pin',
            'Aadhar_No', 'Pan_no', 'project_Location', 'Driving_License', 'DL_issue_Date', 'upload_DL', 'my_file'
        ]
        labels = {
            'Candidate_Name':'Candidate Name',

            'Father_Name':'Fathers Name',
            'Dob':'Date of Birth',
            'Adress':'H.No/Appartment/Villeage',
            'city':'City/District',
            'state':'State',
            'pin':'Pin Code',
            'Aadhar_No':'Aadhar Number',
            'Pan_no':'Pan Number',
            'project_Location':'Project Location',
            'Driving_License':'Driving License',
            'DL_issue_Date':'License Issue Date',
            'upload_DL':'Upload Driving License',
            'my_file':'Upload Joining Form',

        }
        widgets = {
            'Candidate_Name': forms.TextInput(attrs={'class': 'form-control'}),

            'Father_Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Dob': forms.DateInput(attrs={'class': 'form-control','id':'datepicker'}),
            'Adress': forms.Textarea(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-select'}),
            'pin': forms.NumberInput(attrs={'class': 'form-control'}),
            'Aadhar_No': forms.NumberInput(attrs={'class': 'form-control'}),
            'Pan_no': forms.TextInput(attrs={'class': 'form-control'}),
            'project_Location': forms.Select(attrs={'class': 'form-select'}),
            'Driving_License': forms.TextInput(attrs={'class': 'form-control'}),
            'DL_issue_Date': forms.DateInput(attrs={'class': 'form-control','id':'datepicker'}),
            'upload_DL': forms.FileInput(attrs={'class': 'form-control'}),
            'my_file': forms.FileInput(attrs={'class': 'form-control'}),
        }