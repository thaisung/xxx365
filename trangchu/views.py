from django.shortcuts import render
from django.http import HttpResponse
# from .forms import uploadFileForm
from .models import cartoon
from django.core.paginator import Paginator

# Create your views here.
def uploadFile(request):
	pm = cartoon.objects.all()
	return render(request,'trangchu/trangchu.html',{'pm':pm})
def phim(request):
	gm = cartoon.objects.all()
	paginator = Paginator(gm, 9)
	page_number = request.GET.get('page')
	page_obj = paginator.get_page(page_number)
	return render(request,'trangchu/phim1.html',{'page_obj':page_obj})




	# return HttpResponse("hi hi")
# def getFile(request):
# 	if request.method == 'POST':
# 		form = uploadFileForm(request.POST,request.FILES)
# 		if form.is_valid():
# 			instance = upForm(image2=request.FILES['image1'])
# 			instance.save()
# 			# form.save()
# 			return HttpResponse('luu thanh cong')
# 		else:
# 			return HttpResponse('luu ko thanh cong')
# 	else:
# 		return HttpResponse('ko dc roi')

