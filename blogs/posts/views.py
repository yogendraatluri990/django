from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse


# importing constants
from . import  constants

#importing helpers
from . import helper as _util

# Create your views here.
def dashboard(request):
     try:
         sorted_profiles = sorted(constants.POST_CONSTANTS, key=_util.get_date);
         latest_posts = sorted_profiles[:2]
         return render(request, "posts/dashboard.html", {
             'posts': _util.get_modified_list(latest_posts, 'delete')
         })

     except:
          HttpResponse('Not working ')

def allPosts(request): 
     try:
        sorted_list = sorted(constants.POST_CONSTANTS, key=_util.get_date)
        return render(request, "posts/pages/all-posts.page.html", {
            "all_posts": _util.get_modified_list(sorted_list, 'add')
        })
     except:
          HttpResponse("Not working")

def blogDetail(request, slug: str):
        try: 
            current_post = next(post for post in constants.POST_CONSTANTS if post.get('title').lower() == slug.lower())
            return render(request, "posts/pages/post-detail.page.html", {
                "post": current_post
            })
        except:
            HttpResponse('Not Working')
