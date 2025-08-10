from django.shortcuts import render
from .models import PG,PG_Owner,AboutPg,PG_Image

# Create your views here.

def pgs(request):
    pg_items=PG.objects.select_related(
        'owner_name',
        'about',

    ).prefetch_related
    (
        'imgs'
    )
   
   
   

    return render(request,'listing.html',{'pg_items':pg_items})