from django.shortcuts import render, redirect
from .models import Team, PageDeRedirection, TextePageDAccueil
from django.contrib.staticfiles.storage import staticfiles_storage
import os

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, Http404
from .forms import ContactForm
from django.contrib import messages

from pprint import pprint 

# Create your views here.

def home(request):

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'Nouveau contact - Site web' #form.cleaned_data['choices']
            from_email = 'anthony.gagnon@bilodeau.co' #form.cleaned_data['from_email']
            message = 'Nom : ' + form.cleaned_data['name'] + '\nSouhaite discuter de : ' + form.cleaned_data['choices'] + '\nEmail : ' + form.cleaned_data['from_email']  + '\nTelephone : ' + str(form.cleaned_data['phone']) + '\nMessage : ' + form.cleaned_data['message']

            try:
                send_mail(subject, message, from_email, ['anthony.gagnon@bilodeau.co'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            messages.success(request, 'Nous avons bien reçu votre message. Un de nos conseillers vous contactera sous peu.')
            return redirect('home-home')

    clients_urls = []
    for i in list(range(1,24)):
        clients_urls.append(staticfiles_storage.url('img/clients/client-'+str(i)+'.png'))

    texte_accueil = TextePageDAccueil.objects.all()

    #pprint(texte_accueil.first().un_a)
    
    PLACE_HOLDER_TEXT = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    context = {
    'team' : Team.objects.all(),
    'is_mobile' : request.user_agent.is_mobile,
    'form': form,
    'clients_urls' : clients_urls,
    #'texte_accueil' : {'1A' : 'EXPERTISE',
    #                   '1B' : PLACE_HOLDER_TEXT,
    #                   '2A' : 'CONFIANCE',
    #                   '2B' : PLACE_HOLDER_TEXT,
    #                   '3A' : 'TRANSPARENCE',
    #                   '3B' : PLACE_HOLDER_TEXT,    
    #                  }
    'texte_accueil' : {'1A' : texte_accueil.first().un_a,
                       '1B' : texte_accueil.first().un_b,
                       '2A' : texte_accueil.first().deux_a,
                       '2B' : texte_accueil.first().deux_b,
                       '3A' : texte_accueil.first().trois_a,
                       '3B' : texte_accueil.first().trois_b,    
                      }
    }

    return render(request, 'home/home.html', context)

def infolettre_inscription(request):
  return render(request, 'home/infolettre_inscription.html')

def redirection(request, page_de_redirection):
    page_list = PageDeRedirection.objects.all()

    for i in page_list:
        print("EEEEEEEEEEE", i.home_url)
        if i.home_url == page_de_redirection:
            context = {'lien' : i.url,
                       'titre' : i.home_url,
                      }
            return render(request, 'home/page_de_redirection.html', context)

    
    raise Http404('Bad URL')