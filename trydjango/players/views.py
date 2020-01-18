from django.shortcuts import render
import numpy as np
import pandas as pd

# Create your views here.

def data_view(request):
	#obj = Product.objects.get(id=1)
	#context = {
	#	'title': obj.title,
	#	'description': obj.description
	#}

	df = pd.DataFrame(np.random.random((4,4)),
                 index=['exp1','exp2','exp3','exp4'],
                 columns=['Jan2015','Feb2015','Mar2015','Apr2015'])
	print(df.to_json)				 

	context = {
		'object': {"id": 2},
		'title': "some title",
		'data': df.to_json
	}
	return render(request, "players/players.html", context)