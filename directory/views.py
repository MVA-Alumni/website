import random
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.http import Http404
from directory.forms import FormAdd, FormLogin, FormIdentity, FormContact, FormAbout
from directory.models import Alumnus, Year, Domain
import mvaalumni.settings


def home(request):
    return render(request, 'home.html', locals())


def mylogin(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            year = form.cleaned_data["year"]

            token_sent = True

            try:
                user = User.objects.filter(alumnus__year=year).filter(last_name=last_name).get(first_name=first_name)
                subject = 'Login to the MVA Alumni Directory'
                token = default_token_generator.make_token(user)
                mail_message = render_to_string('mail_token.txt', {'user': user, 'token': token, 'PROTOCOL': settings.PROTOCOL, 'DOMAIN': settings.DOMAIN, 'EMAIL_CONTACT': settings.EMAIL_CONTACT})
                send_mail(subject, mail_message, settings.EMAIL_TOKEN, [user.email], fail_silently=True)
            except ObjectDoesNotExist:
                pass
            except MultipleObjectsReturned:
                pass
        else:
            message_error = u"Invalid form !"
    else:
        form = FormLogin()

    EMAIL_CONTACT = settings.EMAIL_CONTACT
    return render(request, 'login.html', locals())


def login_token(request, username, token):
    user = get_object_or_404(User, username=username)
    if default_token_generator.check_token(user, token) == True:
        user.backend = 'django.contrib.auth.backends.ModelBackend' # hack authenticate()
        if user.is_active:
            login(request, user)
        return redirect('home')
    else:
        EMAIL_CONTACT = settings.EMAIL_CONTACT
        return render(request, 'invalidlogin.html', locals())


def mylogout(request):
    logout(request)
    return redirect('home')


@login_required
def search_name(request):
    alumni = Alumnus.objects.none()
    if request.method == 'POST':
        query = request.POST['query']
        bits = query.split()
        for bit in bits:
            alumni = alumni | Alumnus.objects.filter(user__first_name__icontains=bit)
            alumni = alumni | Alumnus.objects.filter(user__last_name__icontains=bit)
    return render(request, 'search_name.html', locals())


@login_required
def search_year(request):
    years = Year.objects.all()
    return render(request, 'search_year.html', locals())


@login_required
def search_domain(request):
    domains = Domain.objects.all()
    return render(request, 'search_domain.html', locals())


@login_required
def search_keyword(request):
    alumni = Alumnus.objects.none()
    if request.method == 'POST':
        query = request.POST['query']
        bits = query.split()
        for bit in bits:
            alumni = alumni | Alumnus.objects.filter(presentation__icontains=bit)
            alumni = alumni | Alumnus.objects.filter(keywords__icontains=bit)
            alumni = alumni | Alumnus.objects.filter(job__icontains=bit)
            alumni = alumni | Alumnus.objects.filter(company__icontains=bit)
    return render(request, 'search_keyword.html', locals())


@login_required
def me_identity(request, success=False):
    alumnus = request.user.alumnus
    MEDIA_URL = settings.MEDIA_URL
    if request.method == 'POST':
        form_identity = FormIdentity(request.POST, request.FILES)
        if form_identity.is_valid():
            alumnus.photo = form_identity.cleaned_data["photo"]
            alumnus.save()
            message_success_identity = u"Identity information successfully updated !"
        else:
            message_error_identity = u"Invalid form !"
    else:
        form_identity = FormIdentity()

    return render(request, 'me_identity.html', locals())


@login_required
def me_contact(request, success=False):
    alumnus = request.user.alumnus
    MEDIA_URL = settings.MEDIA_URL
    if request.method == 'POST':
        form_contact = FormContact(request.POST)
        if form_contact.is_valid():
            request.user.email = form_contact.cleaned_data["email"]
            request.user.save()
            alumnus.phone1 = form_contact.cleaned_data["phone1"]
            alumnus.phone2 = form_contact.cleaned_data["phone2"]
            alumnus.postal = form_contact.cleaned_data["postal"]
            alumnus.website = form_contact.cleaned_data["website"]
            alumnus.save()
            message_success_contact = u"Contact information successfully updated !"
        else:
            message_error_contact = u"Invalid form !"
    else:
        initial = {'email': request.user.email,
            'phone1': alumnus.phone1,
            'phone2': alumnus.phone2,
            'postal': alumnus.postal,
            'website': alumnus.website,
            }
        form_contact = FormContact(initial=initial)

    return render(request, 'me_contact.html', locals())


@login_required
def me_about(request, success=False):
    alumnus = request.user.alumnus
    MEDIA_URL = settings.MEDIA_URL
    if request.method == 'POST':
        form_about = FormAbout(request.POST, request.FILES)
        if form_about.is_valid():
            alumnus.presentation = form_about.cleaned_data["presentation"]
            alumnus.diploma = form_about.cleaned_data["diploma"]
            alumnus.company = form_about.cleaned_data["company"]
            alumnus.job = form_about.cleaned_data["job"]
            alumnus.keywords = form_about.cleaned_data["keywords"]
            #alumnus.domain = form_about.cleaned_data["domain"]
            cv = form_about.cleaned_data["cv"]
            if cv:
                alumnus.cv = cv
            alumnus.save()
            message_success_about = u"Information successfully updated !"
        else:
            message_error_about = u"Invalid form !"
    else:
        initial = {'presentation': alumnus.presentation,
            'diploma': alumnus.diploma,
            'company': alumnus.company,
            'job': alumnus.job,
            'keywords': alumnus.keywords,
            'domain': alumnus.domain,
            }
        form_about = FormAbout(initial=initial)

    return render(request, 'me_about.html', locals())


def create_user(first_name, last_name, gender, email, year, is_staff):
    username = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))
    while User.objects.filter(username=username).exists() == True:
        username = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyz') for i in range(6))
    user = User.objects.create_user(username, email)
    user.first_name = first_name
    user.last_name = last_name
    user.is_staff = is_staff
    user.save()
    alumnus = Alumnus(user=user, year=year, gender=gender)
    alumnus.save()
    subject = 'Access to the MVA Alumni Directory'
    token = default_token_generator.make_token(user)
    mail_message = render_to_string('mail_welcome.txt', {'user': user, 'token': token, 'PROTOCOL': settings.PROTOCOL, 'DOMAIN': settings.DOMAIN, 'EMAIL_CONTACT': settings.EMAIL_CONTACT})
    send_mail(subject, mail_message, settings.EMAIL_TOKEN, [user.email], fail_silently=True)



@staff_member_required
def add(request):
    if request.method == 'POST':
        form = FormAdd(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            email = form.cleaned_data["email"]
            year = form.cleaned_data["year"]

            if User.objects.filter(alumnus__year=year).filter(last_name=last_name).filter(first_name=first_name).exists() == True:
                message_error = u"A user with the same first name, last name and year already exists !"
            else:
                create_user(first_name, last_name, gender, email, year, False)
                form = FormAdd()
                message_success = u"The new alumnus has been added successfully to the database !"
        else:
            message_error = u"Invalid form !"
    else:
        form = FormAdd()

    return render(request, 'add.html', locals())


@staff_member_required
def list_users(request):
    alumni = Alumnus.objects.all()

    alumni_metrics = [
        {
            'username': al.user.username,
            'first_name': al.user.first_name,
            'last_name': al.user.last_name,
            'email': al.user.email,
            'photo': bool(al.photo),
            'presentation': len(al.presentation) if al.presentation else 0,
            'cv': bool(al.cv)
        }
        for al in alumni
    ]

    nb_alumni = len(alumni_metrics)

    return render(request, 'list_users.html', locals())


def first_user(request):
    if User.objects.all():
        raise Http404

    if request.method == 'POST':
        form = FormAdd(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            gender = form.cleaned_data["gender"]
            email = form.cleaned_data["email"]
            year = form.cleaned_data["year"]

            create_user(first_name, last_name, gender, email, year, True)
            return redirect('home')
        else:
            message_error = u"Invalid form !"
    else:
        form = FormAdd()

    return render(request, 'first_user.html', locals())


def contact(request):
    EMAIL_CONTACT = settings.EMAIL_CONTACT
    return render(request, 'contact.html', locals())


@login_required
def alumnus(request, username):
    alumnus = get_object_or_404(Alumnus, user__username=username)
    MEDIA_URL = settings.MEDIA_URL
    return render(request, 'alumnus.html', locals())


@login_required
def year(request, pk):
    year = get_object_or_404(Year, pk=pk)
    alumni = Alumnus.objects.filter(year=year)
    return render(request, 'year.html', locals())


@login_required
def domain(request, pk):
    domain = get_object_or_404(Domain, pk=pk)
    alumni = Alumnus.objects.filter(domain=domain)
    return render(request, 'domain.html', locals())
