from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def properties(request):
    page_property=Listing.objects.all() #import your model
    
    paginator=Paginator(page_property,3)  # 3 here is number of item per page,inshort
    page_number = request.GET.get('page') # checks for page number clicked.
    page_property = paginator.get_page(page_number) #load item according to page number
    
    context = {
        'listings':page_property,
    }
    return render(request,'listings/listings.html',context)
