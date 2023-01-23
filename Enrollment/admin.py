from django.contrib import admin
from .models import Enroll

# Register your models here.
@admin.register(Enroll)
class EnrollmentModelAdmin(admin.ModelAdmin):
    list_display = [
        'Candidate_Name','Father_Name','Dob','Adress','city','state','pin','Aadhar_No','Pan_no','project_Location','Driving_License','DL_issue_Date','upload_DL','my_file'
    ]