from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import render_to_response, get_object_or_404
from myproject.council_pay.models import Councilpay



def home(request):
   all_councils = Councilpay.objects.all().order_by('council')[:50]
   return render_to_response('index.html',{'all_councils':all_councils})
   
def search_form(request):
	
    return render_to_response('search_form.html')   

def council_results(council_list):
		all_councils=council_list
		return render_to_response('index.html', {'all_councils': all_councils})
	
def search(request):
    if 'q' in request.GET:
		term = (request.GET['q']).title()
		search = Councilpay.objects.filter(council__icontains=term)
		
		council_list =[]
		roles = []
		data = []
		for item in search:
		   
		   if item.council not in council_list:
		      council_list.append(item.council)
		print len(council_list)	  
		print council_list
		if len (council_list) ==1:

		   return render_to_response('search.html', {'search':search})
                if len(council_list)>1:
			all_councils = Councilpay.objects.filter(council__in=council_list)
			return render_to_response('index.html', {'all_councils':all_councils})
			
    else:
        message = 'You submitted an empty form.'
        return HttpResponse(message)
