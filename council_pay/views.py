from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import render_to_response, get_object_or_404
from myproject.council_pay.models import Councilpay
from django.db.models import Count



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
		council_index = Councilpay.objects.values('council').annotate(Count('council'))
		#produces query set of all council names with 'council_count' and 'council' attributes
		search = council_index.filter(council__icontains=term)
		
		
		return render_to_response('search.html', {'search':search})
        
			
    else:
        message = 'Whoops! You want to try that again?'
        return HttpResponse(message)

def detail(request):
    choice = request.GET['name']
    print choice
    council = Councilpay.objects.filter(council=choice)
    print council
    return render_to_response('detail.html', {'council': council})
	
def performance(request):
   bonuses = Councilpay.objects.all().exclude(performance_bonus = 0).exclude(role__icontains='Total').exclude(role__icontains='Executive Managers (x6)').order_by('-performance_bonus')
   return render_to_response('bonus.html',{'bonuses':bonuses})
   
def pricey_council(request):
   total_bill = Councilpay.objects.all().filter(role__icontains = "Total Senior Managers of the Municipality").order_by('-total_package')
   return render_to_response('mostpricey.html', {'total_bill': total_bill})   
	
