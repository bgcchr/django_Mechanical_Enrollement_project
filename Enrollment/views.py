from django.shortcuts import render,redirect
from .forms import EnrollForm
from .models import Enroll
from django.views import View
from django.http import HttpResponse,HttpResponseRedirect


# Create your views here.
class HomeView(View):
    def get(self, request):
        form = EnrollForm()
        candidates = Enroll.objects.all()
        return render(request,'Enrollment/home.html', {'candidates':candidates,'form': form})

    def post(self,request):
        form = EnrollForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')






