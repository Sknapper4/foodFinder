from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.contrib.auth.decorators import login_required
from .models import Snack, Store
from .forms import CreateStore, CreateSnack


@login_required()
def index(request):
    snacks = Snack.objects.all()
    stores = Store.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'snacks': snacks,
        'stores': stores
    }
    return HttpResponse(template.render(context, request))


@login_required()
def snack_list(request):
    snacks = Snack.objects.all()[:25]
    template = loader.get_template('food/snack_list.html')
    context = {
        'snacks': snacks
    }
    return HttpResponse(template.render(context, request))


@login_required()
def store_list(request):
    stores = Store.objects.all()
    template = loader.get_template('food/store_list.html')
    context = {
        'stores': stores
    }
    return HttpResponse(template.render(context, request))


@login_required()
def snack_details(request, snack_id):
    snack = get_object_or_404(Snack, pk=snack_id)
    return render(request, 'food/snack_details.html', {'snack': snack})


@login_required()
def store_detail(request, store_id):
    store = get_object_or_404(Store, pk=store_id)
    return render(request, 'food/store_details.html', {'store': store})


@login_required()
def user_snacks(request):
    users_snacks = Snack.objects.filter(snack_author=request.user)
    context = {
        'users_snacks': users_snacks
    }

    return render(request, 'food/my_snacks.html', context)


@login_required()
def create_snack(request):
    if request.method == 'POST':
        form = CreateSnack(request.POST)
        if form.is_valid():
            new_snack = form.save(commit=False)
            new_snack.snack_author = request.user
            new_snack.save()
            return HttpResponseRedirect('/food/')
    else:
        form = CreateSnack()
        return render(request, 'food/create_snack.html', {'form': form})


@login_required()
def create_store(request):
    if request.method == 'POST':
        form = CreateStore(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/food/')
    else:
        form = CreateStore()
        return render(request, 'food/create_store.html', {'form': form})
