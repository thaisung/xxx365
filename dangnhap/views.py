from django.shortcuts import render
from .forms import signupForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.views import View
# from .models import account
# Create your views here.
# def dangnhap(request):
# 	return render(request,'dangnhap/giaodien.html')
# def getFile(request):
# 	if request.method == 'POST':
# 		form = signupForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			return HttpResponse(request.FILES['username'])
# 			instance = account(username1=request.FILES['username'])
# 			instance.save()
# 			instance1 = account(password1=request.FILES['password'])
# 			instance1.save()
# 			return HttpResponse('luu thanh cong')
# 		else:
# 			return HttpResponse('luu ko thanh cong')
# 	else:
# 		return HttpResponse('ko dc roi')
class signupUser(View):
	def get(self,request):
		return render(request,'dangnhap/giaodien.html')
	def post(self,request):
		username = request.POST['username']
		password = request.POST['password']

		user = User.objects.create_user(username,password)
		user.save()
		return HttpResponse('Dang ki thanh cong')