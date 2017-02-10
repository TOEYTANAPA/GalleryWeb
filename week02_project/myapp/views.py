from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from forms import PersonForm
from models import Person, Image
from django.shortcuts import render, redirect
from django.contrib.sessions.models import Session
from django.contrib.sessions.backends.db import SessionStore


from django.shortcuts import render

def home(request):
	img = Image.objects.all()
	

	return render(request, 'gallery.html', {'img': img })



def getImg(request,value):

	pathImg = Image.objects.all()
	i = pathImg.get(id=value)
	listId = request.session.get('key',[])
	listImg = []
	listId.append(value)

	request.session['key'] = listId


	

	for item in listId:
		listImg.append(pathImg.get(id=item))
	
	if len(listId)== 1:		
		request.session.set_expiry( 60 )




	return render(request, 'bigimg.html',
		{
	
			'list': i,
			'session': request.session.get('key'),
			'listId': listId,
			'listImg' : listImg
		})



class CreatePersonView(CreateView):
	queryset = Person()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class UpdatePersonView(UpdateView):
	queryset = Person.objects.all()
	template_name='person.html'
	form_class = PersonForm
	success_url = '/'

class ListPersonView(ListView):
    model = Person
    template_name='person_list.html'

