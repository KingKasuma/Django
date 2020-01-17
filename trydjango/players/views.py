from django.shortcuts import render

# Create your views here.

def data_view(request):
	#obj = Product.objects.get(id=1)
	#context = {
	#	'title': obj.title,
	#	'description': obj.description
	#}
	context = {
		'object': {"id": 2},
		'title': "some title"
	}
	return render(request, "players/players.html", context)