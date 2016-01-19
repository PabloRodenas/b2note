from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from .models import Annotation


def index(request):
    return HttpResponse("replace me with index text")



def typeahead(request):
     print "type ahead"
     return render_to_response('searchapp/search.html')


def ontology_search(request):
    print "onto search"
    context = RequestContext(request)
    context_dict = {}
    if request.method == 'GET':
        print 'pressed'
        print request
        #search_string = request.GET['query']
        #print request.GET['query']

        # Adds our results list to the template context under name pages.
        #context_dict['search_string'] = search_string

    return render_to_response('searchapp/search.html', context_dict, context)

def hostpage(request):
    return render(request, 'searchapp/hostpage.html', {'iframe_on': 350})


# forbidden CSRF verification failed. Request aborted.
@csrf_exempt
def interface_main(request):
    annotation_list = Annotation.objects.all()
    #triple_list = Triple.objects.all()
    if request.POST.get('ontology_json'):
            print request.POST.get('ontology_json')
	    print request.POST.get('subject_tofeed')


    if request.POST.get('subject_tofeed')==None:
        context = RequestContext(request, {
            #'triple_list': triple_list,
	    'annotation_list': annotation_list,
            'subject_tofeed': ""
        })
    else:
        print request.POST.get('subject_tofeed')
        context = RequestContext(request, {
            #'triple_list': triple_list,
	    'annotation_list': annotation_list,
            'subject_tofeed': request.POST.get('subject_tofeed'),
        })
    return render_to_response('searchapp/interface_main.html', context)
 