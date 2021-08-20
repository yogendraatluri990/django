from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


# importing constants
from . import  constants

# Create your views here.
def dashboard(request):
     try:
         return render(request, "posts/dashboard.html", {
             "page_title": f"welcome to {constants.POST_CONSTANTS.get('index_title')}",
             "intro_card_title": f"{constants.POST_CONSTANTS.get('intro_card_title')}",
             "profile_content": f"{constants.POST_CONSTANTS.get('profile_content')}"
         })

     except:
          HttpResponse('Not working ')

def allPosts(request): 
     try:
        return render(request, "posts/pages/all-posts.page.html", {})
     except:
          HttpResponse("Not working")

def blogDetail(request):
        try: 
            return render(request, "posts/pages/blog-detail.page.html", {})
        except:
            HttpResponse('Not Working')
