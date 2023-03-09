from webapp.models import Task
from webapp.forms import TaskForm
from django.views.generic import DeleteView, CreateView, UpdateView
from django.urls import reverse, reverse_lazy


class TaskCreateView(CreateView):
    template_name = 'task_create.html'
    model = Task
    form_class = TaskForm

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDetail(DeleteView):
    template_name = 'task.html'
    model = Task


class TaskUpdateView(UpdateView):
    template_name = 'task_update.html'
    form_class = TaskForm
    model = Task

    def get_success_url(self):
        return reverse('task_detail', kwargs={'pk': self.object.pk})


class TaskDeleteView(DeleteView):
    template_name = 'task_confirm_delete.html'
    model = Task
    success_url = reverse_lazy('index')
