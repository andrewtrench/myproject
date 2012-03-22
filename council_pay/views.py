from django.conf.urls.defaults import *
from django.http import HttpResponse
from django.views.generic import DetailView, ListView
from django.shortcuts import render_to_response, get_object_or_404
from myproject.council_pay.models import Councilpay, Geo
from django.db.models import Count, Q
from pylab import *





def home(request):
   all_councils = Councilpay.objects.all().order_by('council')[:50]
   return render_to_response('index.html',{'all_councils':all_councils})
   
def search_form(request):
    points = Geo.objects.all()
    return render_to_response('search_form.html', {'points': points})   

def council_results(council_list):
		all_councils=council_list
		return render_to_response('index.html', {'all_councils': all_councils})
	
def search(request):
    if 'q' in request.GET:
		term = (request.GET['q']).title()
		council_index = Councilpay.objects.values('council').annotate(Count('council'))
		#produces query set of all council names with 'council_count' and 'council' attributes
		search = council_index.filter(council__icontains=term)
		council_code = ''
		for item in search:
		   
		   code = item['council'].split('(')[1].replace(')','')
		   item['code']=code
		   
		
		return render_to_response('search.html', {'search':search})
        
			
    else:
        message = 'Whoops! You want to try that again?'
        return HttpResponse(message)
	

def detail(request, code):
    #this view displays the detail of the municipality
	
    new_code = code # variable used for looking up the concil code in the geo database with table with gis co-ords
    code = "("+code+")" #put the brackets back to make the search easier
    
    council = Councilpay.objects.filter(council__icontains=new_code).order_by('-total_package')
    
    name = council[1].council.split('(')[0]
    province = council[1].province
    
    council_loc = Geo.objects.filter(code=new_code)
    if len(council_loc)==0:
	   lat = '-31.288566'
	   lng = '24.477539'
	   zoom = 5
	   message = "Sorry. Can't map that council"
	   area = ""
	   population = ""
    if len(council_loc)>0:
	   lat = council_loc[0].lat
           lng = council_loc[0].lng
           message = "The main urban centre of the council"
           zoom = 11
           area = council_loc[0].area
           population = council_loc[0].population
		 
    		 
   	
	
	
	  
    return render_to_response('detail.html', {'council': council, 
	'name':name,
	'province':province,
	'lat':lat,'lng':lng,
	'message':message,
	'zoom':zoom,
	'area': area,
	'population': population,
	
	
	})
	
def performance(request):
   bonuses = Councilpay.objects.all().exclude(performance_bonus = 0).exclude(number__gt = 2).exclude(role__icontains='Total').exclude(role__icontains='Executive Managers (x6)').order_by('-performance_bonus')
   return render_to_response('bonus.html',{'bonuses':bonuses})
   
def pricey_council(request):
   total_bill = Councilpay.objects.all().filter(role__icontains = "Total Senior Managers of the Municipality").order_by('-total_package')
   return render_to_response('mostpricey.html', {'total_bill': total_bill}) 
   
def mayors(request):
   mayors = Councilpay.objects.filter(Q(role = "Executive Mayor") | Q(role = "Mayor")).order_by('-total_package')
   
   
   return render_to_response('mayors.html',{'mayors':mayors})

def mm(request):
   mm = Councilpay.objects.filter(Q(role = "Municipal Manager (MM)") | Q(role = "City Manager")).order_by('-total_package')
   
   
   return render_to_response('mm.html',{'mm':mm})   
   
def total_exec(request):
   executives = Councilpay.objects.filter(role = 'TOTAL COST OF COUNCILLOR, DIRECTOR and EXECUTIVE REMUNERATION').order_by('-total_package')
   
   
   return render_to_response('exec.html',{'executives':executives})   

   
def graph(request):
   return render_to_response('detail_graph.html')   

def test(request):
   'Display map'
   return render_to_response('test.html', {})
   


def google_map(request):
    points = Geo.objects.all()
    	
    return render_to_response('google_maps.html',
                              {'points': points,})
	
