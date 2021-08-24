from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .models import post
from .forms import CpostFORMS
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.conf import settings

# =======================================Create your post logic (here)==================-==============================    Images =request.FILES['Images']       Category=request.POST['CategoryF']
def createVIEW(request):
  if request.method == 'POST':
    form = CpostFORMS(request.POST, request.FILES)
    if form.is_valid():
      new_req = post(User_Name = request.user,Title=request.POST['TitleF'],Details = request.POST['DetailsF'],)
      new_req.save()
      return HttpResponseRedirect(reverse('test'))

  else:
    form = CpostFORMS()
  
  context = {'form': form}
  return render(request,'createPost.html', context)



# =======================================Details post logic (here)======================================================

def detailsVIEW(request, id):           #views logic...
  content = post.objects.filter(id=id)       
  return render(request,'details.html', {'content': content})



# =======================================Delete post logic (here)=======================================================

class DeleteVIEW(DeleteView):
  model = post
  template_name = 'delete.html'
  context_object_name = 'object'
  success_url = reverse_lazy('index')


# =======================================History post logic (here)=======================================================

def WhistoryVIEW(request):
  Hposts = post.objects.all().filter(User_Name=request.user)
  return render(request, 'whistory.html', {'Hposts' : Hposts})