from django.db import models

# Create your models here.
location=[
('Odisha','Odisha'),
('Hathras','Hathras'),
('Aligarh','Aligarh'),
('Bptp','Bptp'),
('Imt_Faridabad','Imt_Faridabad'),
('Mcf','Mcf'),
('Dwarka','Dwarka'),
('Ashok Vihar','Ashok Vihar'),
('Jhansi','Jhansi'),
('Imlota','Imlota'),
('Head Office','Head Office'),
('Rajasthan','Rajasthan'),
('Behror','Behror'),
('Bhopal','Bhopal'),
('Sehore','Sehore'),
('Jhajjar','Jhajjar'),
('Barwala','Barwala'),
('Puran Pur','Puran Pur'),
('Nagar','Nagar'),
('Jaisalmer','Jaisalmer'),
('Kostnallah','Kostnallah'),
('Rpd-1','Rpd-1'),
('Guhana-Sonepat-II','Guhana-Sonepat-II'),
('Jalaun','Jalaun'),
('Jind-Guhana-I','Jind-Guhana-I'),
]

STATE=[
('Delhi','Delhi')
]


class Enroll(models.Model):
    Candidate_Name = models.CharField(max_length=50)

    Father_Name = models.CharField(max_length=50)
    Dob = models.DateField()
    Adress=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(choices=STATE,max_length=50)
    pin=models.PositiveIntegerField()
    Aadhar_No = models.PositiveIntegerField()
    Pan_no = models.CharField(max_length=10)
    project_Location = models.CharField(choices=location, max_length=100)
    Driving_License = models.CharField(max_length=25)
    DL_issue_Date = models.DateField()
    upload_DL = models.ImageField(upload_to='Dlimg', blank=True)
    my_file = models.FileField(upload_to='Doc', blank=True)








