from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    now = datetime.now()
    # # Number of visits to this view, as counted in the session variable.
    # num_visits = request.session.get('num_visits', 1)
    # request.session['num_visits'] = num_visits + 1
    context={"now": now,

             }

    return render(request, 'home.html', context=context)