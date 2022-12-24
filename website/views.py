from django.shortcuts import render
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages


# Create your views here.
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        new_form = form.save(commit=False)
        name = "unknown"
        new_form.name = name
        if form.is_valid():
            new_form.save()
            messages.add_message(request, messages.SUCCESS, 'Your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your ticket did not submitted')
    
    form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return HttpResponseRedirect('/')

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    
    form = ContactForm()
    return render(request, 'website/test.html', {'form': form})

