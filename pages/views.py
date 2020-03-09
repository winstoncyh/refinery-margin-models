from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views import generic
from core_models.models import FeedstockProductSlateCombination,RefineryProcessUnit,RefinedProduct,CrudeFeedstock
from graphviz import Digraph
import os
import json
from django.core.serializers.json import DjangoJSONEncoder


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Create your views here.

def home_view(request, *args,**kwargs):
    template_context_dictionary = {'list_of_crude_streams':['Dubai','Cossack','Enfield','Forties']}
    return render (request,'home.html',template_context_dictionary)

def about_view(request, *args,**kwargs):
    my_context = {
        'my_address':'Singapore',
        'my_number' : 935565451,
    }
    return render (request,'about.html',my_context)

def margin_home_view(request,region='ALL'):
    # Initialize and/or read variables from HTTP POST/GET for margins page
    refined_products_yield_tuple_list = []
    refinery_unit_with_primary_crude_feedstock =[]
    FeedstockProductSlateCombination_value_list=[]
    region = region.strip().upper()
    # Get the region value from the URL passed, default is SEA. Regions in viewer are hard coded for now
    regions_dict = {
        'NEA': "North East Asia",
        'AGI': "Arabian Gulf/India",
        'SEA': "South East Asia",
        'MARGINS': 'ALL',
        'ALL': 'ALL'
    }
    selected_region = regions_dict.get(region)




    # get all margins tagged to region from db, returns query set
    if selected_region.upper().strip() in ('ALL','MARGINS'):
        rpu_objects_qs = RefineryProcessUnit.objects.all()
    else:
        rpu_objects_qs = RefineryProcessUnit.objects.filter(country__country_region_name__region_name__iexact=selected_region)
    # Get tuple values list from queryset
    rpu_objects_value_list = rpu_objects_qs.values_list()

    print(rpu_objects_value_list)

    # return HttpResponse('Region is ' + region)

    # retrieve post request to return relevant objects
    if request.method == 'GET':
        try:
            selected_rpu_value = str(request.GET.get('selected_rpu'))
            selected_fsps_value = str(request.GET.get('selected_fsps'))

            print('selected_rpu_value is ' + selected_rpu_value)
            print('selected_fsps_value is ' + selected_fsps_value)


            # get first level feedstock of selected rpu
            if FeedstockProductSlateCombination.objects.filter(refinery_processing_unit__name=selected_rpu_value):
                print('FeedstockProductSlateCombination found')
                FeedstockProductSlateCombination_QS = FeedstockProductSlateCombination.objects.filter(refinery_processing_unit__name=selected_rpu_value)
                FeedstockProductSlateCombination_value_list = FeedstockProductSlateCombination_QS.values_list()
                FeedstockProductSlateCombination_dict_list = list(FeedstockProductSlateCombination_QS.values())
                # response = JsonResponse(FeedstockProductSlateCombination_dict_list, safe=False)
                FeedstockProductSlateCombination_json = json.dumps(FeedstockProductSlateCombination_dict_list, cls=DjangoJSONEncoder)
                print('json is' + FeedstockProductSlateCombination_json)
                return JsonResponse(FeedstockProductSlateCombination_json,safe=False)


        except Exception as e:
            print('Exception occurred details here: ' + str(e))

    print('Setting django  context variables...')
    # set django context variable
    my_context = {
        'my_region':region,
        'my_number' : 935565451,
        'rpu_objects_value_list': rpu_objects_value_list,
        'selected_region':selected_region,
        'refined_products_yield_tuple_list':refined_products_yield_tuple_list,
        'feedstock_slate_combi_value_list': FeedstockProductSlateCombination_value_list
    }

    # get all feedstocks for rpu

    # get all refined products for rpu

    g = Digraph('G', filename='cluster.gv')


    # region Generate SVG graph of refined products hierarchy, using a cluster graph saved into svg format
    g = Digraph('G', filename='cluster.gv')

    # NOTE: the subgraph name needs to begin with 'cluster' (all lowercase)
    #       so that Graphviz recognizes it as a special cluster subgraph

    # Get

    with g.subgraph(name='cluster_0') as c:
        c.attr(style='filled', color='lightgrey')
        c.node_attr.update(style='filled', color='white')
        c.edges([('test', 'a1'), ('a1', 'a2'), ('a2', 'a3')])
        c.attr(label='process #1')

    with g.subgraph(name='cluster_1') as c:
        c.attr(color='blue')
        c.node_attr['style'] = 'filled'
        c.edges([('b0', 'b1'), ('b1', 'b2'), ('b2', 'b3')])
        c.attr(label='process #2')


    # g.node('start', shape='Mdiamond')
    # g.node('end', shape='Msquare')

    # >> > lname = 'Doe'
    # >> > Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])

    # outputs gv file containing soure code describing the nodes, AND the output file in desired format
    # NOTE THAT SVGS MUST BE RENDERED AS PART OF HTML CODE BY USING TEMPLATE TAG {{% INCLUDE 'xxx.svg' %}},
    # LOADING SVG IN IMG TAG IS INADEQUATE AND SVG LINKS WILL NOT WORK
    # g.render('static/images/product-tree.gv', view=False,format='svg')

    g.render('templates/svg/product-tree.gv', view=False, format='svg')
    # endregion




    return render (request,'margins.html',my_context)

# def get_name_view(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')
#
#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()
#
#     return render(request, 'name.html', {'form': form})

class IndexView(generic.ListView):
    template_name = 'margins.html'
    context_object_name = 'margin_list'