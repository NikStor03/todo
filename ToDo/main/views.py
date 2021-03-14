from django.shortcuts import render
from django.http import HttpResponseRedirect as redirect
from django.views.generic import View

from .forms import *
from .models import *

class BaseView(View):

    def get(self, request, *args, **kwargs):
        todos = ToDo.objects.all()
        list = []
        for todo in todos:
            if len(todo.content) >= 35:
                cont = todo.content
                list.append({
                    'title': todo.title,
                    "cont": f"{cont[0:36]}..."
                })
            else:
                cont = todo.content
                list.append({
                    'title': todo.title,
                    "cont": cont
                })
        todos = todos[::-1]
        context = {
            'todos': todos,
            'content': list,
        }

        return render(request, 'main/base.html', context)

class OnDeleteView(View):

    def get(self, request, *args, **kwargs):
        slug = kwargs.get('slug')
        todo = ToDo.objects.filter(slug=slug)
        todo.delete()
        return redirect('/')

class OnAddView(View):

    def get(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        context = {
            'form': form,
        }
        return render(request, 'main/add_new.html', context)

    def post(self, request, *args, **kwargs):
        form = TodoForm(request.POST or None)

        if form.is_valid():
            new_todo = form.save(commit=False)
            new_todo.title = form.cleaned_data['title']
            new_todo.content = form.cleaned_data['content']
            new_todo.time = form.cleaned_data['time']
            new_todo.slug = form.cleaned_data['title'].replace(' ', '+')
            new_todo.save()
            return redirect('/')
        return redirect('/add')

class TodoInfoView(View):

    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs)
        slug = kwargs.get("slug")
        todo = ToDo.objects.filter(slug=slug)
        context = {
            'todo': todo,
        }
        return render(request, 'main/info.html', context)
