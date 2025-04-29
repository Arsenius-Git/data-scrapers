from django.shortcuts import render, redirect
from .forms import CreateOffer, RegisterForm, LookingForOffer
from .models import create_model, looking_for_offers

# Create your views here.
def home(request):
    jobs = create_model.objects.all()
    cv = looking_for_offers.objects.all()
    if request.method == 'POST' and 'delete_job' in request.POST:
        job_id = request.POST.get('delete_job')
        try:
            job = create_model.objects.get(id=job_id)
            job.delete()
            return redirect('home')
        except create_model.DoesNotExists:
            print("the error")
    if request.method == 'POST' and 'delete_cv' in request.POST:
        cv_id = request.POST.get('delete_cv')
        try:
            cv = looking_for_offers.objects.get(id=cv_id)
            cv.delete()
            return redirect('home')
        except create_model.DoesNotExists:
            print("the error")
    context = {'jobs': jobs,
               'cv':cv}
    return render(request,'main/home.html', context)

def create_offer(request):
    if request.method == 'POST':
        form = CreateOffer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateOffer()

    context = {'form':form}
    return render(request, 'main/create_offer.html', context)
def job_list(request):
    jobs = create_model.objects.all()
    context = {'jobs':jobs}
    return render(request, 'main/home.html', context)
def create_cv(request):
    if request.method == 'POST':
        form = LookingForOffer(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LookingForOffer()
    context = {'form':form}
    return render(request, 'main/create_cv.html', context)
def cv_list(request):
    cv = looking_for_offers.objects.all()
    context = {'cv':cv}
    return render(request, 'main/home.html', context)


def register(response):
    if response.method == 'POST':
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("login")
    else:
        form = RegisterForm()
    context = {'form':form}
    return render(response, "main/register.html", context)

