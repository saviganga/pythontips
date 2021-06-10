import csv
import io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import permission_required, login_required
from django.views.decorators.http import require_http_methods, require_safe
from .models import Tweet
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from datetime import datetime
from .forms import PostTipsForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.


@permission_required('admin.can_add_log_entry')
def sync_db(request):

    """sync csv database to django models"""

    template = 'tips/sync_db.html'
    prompt = {'prompt': 'upload csv file'}

    if request.method == 'GET':
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'selected file not csv')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)


    for col in csv.reader(io_string):

        #date_time_obj = datetime.strptime(col[0], '%m/%d/%Y %H:%M:%S')

        _, created = Tweet.objects.update_or_create(
            username=col[2],
            tip=col[1],
            email=col[3],
            created_at=datetime.strptime(col[0], '%m/%d/%Y %H:%M:%S'),
        )

    context = {}
    return render(request, template, context)



def index(request):

    """homepage. contains the search bar"""

    template = 'tips/display_tips.html'
    python_tips = Tweet.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(python_tips, 20)
    try:
        tweets = paginator.page(page_number)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    context = {'tweets': tweets}
    return render(request, template, context)


def search_result(request):

    template = 'tips/search_result.html'
    searchword = request.GET.get('query', False)
    python_tips = Tweet.objects.filter(tip__contains=searchword)
    page_number = request.GET.get('page')
    paginator = Paginator(python_tips, 20)

    try:
        tweets = paginator.page(page_number)
    except PageNotAnInteger:
        tweets = paginator.page(1)
    except EmptyPage:
        tweets = paginator.page(paginator.num_pages)

    context = {'tweets': tweets, 'searchword': searchword}
    return render(request, template, context)


@login_required()
def post_tip(request):

    template = 'tips/post_tip.html'
    form = PostTipsForm()
    context = {'form': form}

    if request.method == 'POST':
        form = PostTipsForm(request.POST)

        if form.is_valid():
            new_tip = form.save(commit=True)
            new_tip.save()
            return redirect('homepage')

    return render(request, template, context=context)


def signup(request):

    template = 'tips/signup.html'
    form = UserCreationForm()
    context = {'form': form}

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():

            user = form.save()
            '''
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            '''
            login(request, user)
            return redirect('homepage',)

    return render(request, template, context)