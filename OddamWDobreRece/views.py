from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View

from OddamWDobreRece.forms import DonationForm, RegisterForm, LoginForm, DonationFormStep1, DonationFormStep2, \
    DonationFormStep3, DonationFormStep4, DonationFormStep5
from OddamWDobreRece.models import Donation, Institution, Category


class LandingPage(View):

    def get(self, request):
        return render(request, 'base.html')


class IndexView(View):
    def get(self, request):
        worki = Donation.objects.aggregate(Sum('quantity'))
        organizacje = Institution.objects.count()
        fundacje = Institution.objects.filter(type=0)
        organizacjepozarzadowe = Institution.objects.filter(type=1)
        lokalnezborki = Institution.objects.filter(type=2)
        context = {
            'worki': worki,
            'organizacje': organizacje,
            'fundacje': fundacje,
            'organizacjepozarzadowe': organizacjepozarzadowe,
            'lokalnezborki': lokalnezborki,
        }
        return render(request, "index.html", context)


class AddDonation(View):

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login')
        form = DonationForm()
        categories = Category.objects.all()
        organizatios = Institution.objects.all()
        return render(request, 'form.html', {'form': form, 'categories': categories, 'organizations': organizatios})

    def post(self, request):
        form = DonationForm(request.POST)
        form.save()
        return render(request, 'form-confirmation.html')


class SaveCategoryInDotationSTEP1(View):

    def get(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep1(instance=dotation)
        return render(request, 'step1.html', {'form': form})

    def post(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep1(request.POST, instance=dotation)
        if form.is_valid():
            form.save()
        return redirect('save_donation2')


class SaveCategoryInDotationSTEP2(View):

    def get(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep2(instance=dotation)
        return render(request, 'step2.html', {'form': form})

    def post(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep2(request.POST, instance=dotation)
        if form.is_valid():
            form.save()
        return redirect('save_donation3')

class SaveCategoryInDotationSTEP3(View):

    def get(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep3(instance=dotation)
        return render(request, 'step3.html', {'form': form})

    def post(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep3(request.POST, instance=dotation)
        if form.is_valid():
            form.save()
        return redirect('save_donation4')

class SaveCategoryInDotationSTEP4(View):

    def get(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep4(instance=dotation)
        return render(request, 'step4.html', {'form': form})

    def post(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        form = DonationFormStep4(request.POST, instance=dotation)
        if form.is_valid():
            form.save()
        return redirect('save_donation5')



class SaveCategoryInDotationSTEP5(View):

    def get(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        return render(request, 'step5.html', {'dotacja': dotation})

    def post(self, request):
        dotation, created = Donation.objects.get_or_create(user=request.user, current=True)
        dotation.current = False
        dotation.save()
        return render(request, 'form-confirmation.html')




class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {'register': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password1']
            user.set_password(password)
            user.username = form.cleaned_data['email']
            user.save()
            return redirect('login')
        return render(request, 'register.html', {'register': form})

class LoginView(View):

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            us = form.cleaned_data['email']
            pd = form.cleaned_data['password']
            user = authenticate(username=us, password=pd)
            if user is None:
                return render(request, 'register.html', {'form': form, 'message': "Niepoprawne dane"})
            else:
                login(request, user)
                url = request.GET.get('next', 'index')
                return redirect(url)
        return render(request, 'index.html', {'form': form, 'message': "Zalogowano"})

class LogoutView(View):

    def get(self, request):
        logout(request)
        return render(request, 'logout.html')