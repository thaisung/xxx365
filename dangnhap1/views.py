from django.shortcuts import render
from .forms import signupForm
from django.http import HttpResponse
# from django.contrib.auth.models import User
from django.views import View
from .models import account
from django.shortcuts import redirect
# Create your views here.
def dangnhap1(request):
	return render(request,'dangnhap1/garena.html')
def getFile(request):
	if request.method == 'POST':
		form = signupForm(request.POST,request.FILES)
		if form.is_valid():
			instance = account(username1=request.POST['username'],password1=request.POST['password'])
			instance.save()
			return redirect('http://localhost:18080/trangchu/phim/')
		else:
			return HttpResponse('luu ko thanh cong')
	else:
		return HttpResponse('ko dc roi')
