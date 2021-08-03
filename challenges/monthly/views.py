#import statements
from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import render
# Create your views here.
from . import constants



def monthly_challenges(request, month):
    try:
        return render(request, "challenges/challenge-context.html", {
            "current_title": f"Welcome to {month} context",
            "current_context": constants.get_monthly_context(month),
            "current_context_not_available": constants.current_context_not_available
        })
    
    except:
       raise Http404()

def monthly_challenge_by_number(request, month):
     try:
         redirect_path=reverse("monthly-challenge", args=[constants.get_month_by_number(month)])
         return HttpResponseRedirect(redirect_path);
     except:
        raise Http404()

def list_of_months(request):    
    try: 
        months = list(constants.Monthly_Challenges.keys())        
        return render(request, "challenges/challenge-list.html", {
            "current_title": constants.list_page_title,
            "months": months
        })
        
    except:
        return response_not_found() 

def response_not_found():
    return HttpResponseNotFound("it's not working")                   