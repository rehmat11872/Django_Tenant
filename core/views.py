from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .models import *
# Create your views here.
def home_view(request):
    items = Item.objects.all()
    context = {
      "items":items
    }
    return render(request, 'home.html', context)



class CreateItemView(View):
    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        if name:
            item = Item(name=name)
            item.save()
            return HttpResponse(f'<li class="text-4xl font-thin">{ item.name }</li>')
        else:
            return redirect('home')

    def get(self, request, *args, **kwargs):
        return redirect('home')