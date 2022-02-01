from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from blog.models import Post, Comment
from django.views import generic
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
import logging
logger = logging.getLogger(__name__)

    
def index(request):
    now = datetime.now()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {"now": now, "num_visits": num_visits}
    return render(request, 'index.html', context=context)