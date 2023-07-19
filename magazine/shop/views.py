from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from .forms import SubscribersForm, RegisterUserForm, ZamerUserForm
from products.models import *
from django.contrib.auth import login
from django.template import loader
from .models import Stati
from .utils import DataMixin
from .forms import FeedBackForm
# from .models import Comment
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError


# Create your views here.
def landing(request):
    name = 'CodingMedVed'
    current_day = '21.03.2023'
    form = SubscribersForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # form = SubscribersForm(request.POST)
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data
        print(data['name'])

        new_form = form.save()

    return render(request, 'orders/landing.html', locals())

def catalog(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    return render(request, 'shop/catalog.html', locals())

def home(request):
    products_images = ProductImage.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_windows = products_images.filter(product__category_id=1)
    products_images_door = products_images.filter(product__category_id=2)
    return render(request, 'shop/home.html', locals())

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация ")
        return dict(list(context.items()) + list(c_def.items()))


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация ")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')



class FeedBackView(DataMixin, FormView):
    form_class = FeedBackForm
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


def stati(request):
    template = loader.get_template('statii.html')
    context = {
        'content': 'content',
    }
    return HttpResponse(template.render(context, request))

def show_post(request):
    return render(request, 'post.html')



class ZamerView(DataMixin, FormView):
    form_class = ZamerUserForm
    template_name = 'zamer.html'
    success_url = reverse_lazy('home')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Заявка для бесплатного замера")
        return dict(list(context.items()) + list(c_def.items()))


def nas(request):
    return render(request, 'onas.html')
