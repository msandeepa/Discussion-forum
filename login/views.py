from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.template import RequestContext, loader
from django.http import Http404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import Post
from django.views import generic
from django.template import RequestContext
from django.template.context_processors import csrf
from django.shortcuts import redirect



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )           
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
 
    return render_to_response(
    'registration/register.html',
    variables,
    )
def Homepage(request):
    return render(request,'Bootstrap/Homepage.html')


def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    return render_to_response(
    'home.html',
    { 'user': request.user }
    )
def forum(request):
   if request.method == 'POST':
       user_form = questionForm(request.POST)
       if user_form.is_valid():
           user = user_form.save()
           # user.set_password(user.password)
           user.save()
           # user_form.save();
           # new_user = user_form.save(profile_callback=profile_callback)
           return HttpResponseRedirect('/home/')
   else:
       user_form = questionForm()
   variables = RequestContext(request, {
   'form': user_form
   })

   return render_to_response(
   'registration/askquestion.html',
   variables,
   )
class java(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(subject='Java')

class dbms(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(subject='DBMS')

class wp(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(subject='WebProgramming')

class General(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(subject='General')

def Profilepage(request):
    return render(request,'Bootstrap/Profilepage.html')

class IndexView(generic.ListView):
    template_name = 'home.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Post.objects.filter(subject='Datastructure')
def index(request):
    latest_question_list = Post.objects.order_by('-subject')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'ds.html', context)
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_new(request):
    form = questionForm()
    return render(request, 'post_edit.html', {'form': form})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = questionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/home/')
    else:
        form = questionForm()
    return render(request, 'post_edit.html', {'form': form})