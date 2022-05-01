
from datetime import datetime
import email
from re import S, template
from django import forms
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
import django
from .models import Task
from datetime import datetime
from django.contrib.auth.models import User
# Create your views here.

class ToDoList(ListView):
    model = Task
    template_name = 'todo/HomePage.html'
    context_object_name = 'tasks'


class ItemForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'date','user']
    def __init__(self, *args, **kwargs):
            super(ItemForm, self).__init__(*args, **kwargs)
            self.fields['date'].initial= django.utils.timezone.now


class MainApp(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'todo/AppPage.html'
    context_object_name = 'tasks'

    def post(self, *args, **kwargs):
            return self.get(*args, **kwargs)

    def get_context_data(self,**kwargs):
        context = super(MainApp, self).get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['IncompleteCount'] = context['tasks'].filter(complete=False).count() 
        context['completeCount'] = context['tasks'].filter(complete=True).count() 
        context['form'] = ItemForm(self.request.POST)
        #context['form'].instance.user = self.request.user
        

        print(context['form'].data.get("title"))
        print(context['form'].data.get("date"))

        if(context['form'].is_valid() ):
            a = context['form'].save(commit=False)
            a.date = django.utils.timezone.now()
            a.user = self.request.user # Set the user object here
            a.save()


        return context



class TaskDetail(DetailView):
    model = Task
    template_name = 'todo/DetailPage.html'
    
class CreateTask(CreateView):    
    model = Task
    fields = ['title','description','email','notification','complete']
    success_url = reverse_lazy('todo:app')
    template_name = 'todo/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

class UpdateTask(UpdateView):
    model = Task
    fields = ['title','description','complete','email','notification']
    success_url = reverse_lazy('todo:app')
    template_name = 'todo/create.html'    

class DeleteTask(DeleteView):
    model = Task
    success_url = reverse_lazy('todo:app')
    template_name = 'todo/DeletePage.html'  

class MyLogin(LoginView):
    template_name = 'todo/LoginPage.html'
    fields = 'user'
    redirect_authenticated_user = True

    def get_success_url(self):
    	return reverse_lazy('todo:app')
    

class MyLogout(LogoutView):
    template_name = 'todo/LogoutPage.html'
    fields = '__all__'


class RegisterForm(forms.ModelForm):
    username = forms.CharField(required=True)
    email = forms.CharField(required=False)
    password = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ['username','email','password']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})

    def __init__(self,*args, **kwargs):
            super().__init__(**kwargs)
            self.fields['username'].widget.attrs.update({
                'name':'username',
                'type':'text',
                'class':'form-control',
                'placeholder':'UserName',
            })

            self.fields['email'].widget.attrs.update({
                'name':'password',
                'type':'email',
                'class':'form-control',
                'placeholder':'Email',
            })
            self.fields['password'].widget.attrs.update({
                'name':'password',
                'type':'password',
                'class':'form-control',
                'placeholder':'Password',
            })


class MyRegister(FormView):
    template_name = 'todo/RegisterPage.html'
    form_class = RegisterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('todo:app')

    

    


    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(MyRegister,self).form_valid(form)

    ## to redirect before registeration
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('todo:app')
        return super(MyRegister,self).get(*args,**kwargs)


def about(request):
    return render(request,'todo/About.html')

def contact(request):
    return render(request,'todo/Contact.html')

def donate(request):
    return render(request,'todo/Donate.html')