from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from todoapps.models import Tasktodo
from .forms import TodoForm

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView


class TaskListview(ListView):
    model = Tasktodo
    template_name = 'home.html'
    context_object_name = 'task'


class TaskDetailview(DetailView):
    model = Tasktodo
    template_name = 'detail.html'
    context_object_name = 'task'


class Taskupdateview(UpdateView):
    model = Tasktodo
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name', 'priority', 'date')

    def get_success_url(self):
        return reverse_lazy('todoapps:cbvdetail', kwargs={'pk': self.object.id})

class TaskDeleteview(DeleteView):
    model = Tasktodo
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvhome')



def todo(request):
    task = Tasktodo.objects.all()
    if request.method == 'POST':
        name = request.POST.get('task', '')
        priority = request.POST.get('priority', '')
        date = request.POST.get('date', '')
        task = Tasktodo(name=name, priority=priority, date=date)
        task.save()
    return render(request, "home.html", {'task': task})


def delete(request, taskid):
    task = Tasktodo.objects.get(id=taskid)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request, 'delete.html')


def update(request, id):
    task = Tasktodo.objects.get(id=id)
    f = TodoForm(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request, 'edit.html', {'f': f, 'task': task})

# def details(request):
#     task1=Tasktodo.objects.all()
#     return render(request,'details.html',{'task1':task1})
