from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView

from apps.forms import RegisterForm
from apps.mixins import NotLoginRequiredMixin
from apps.models import UserView


class SimpleView(ListView):
    template_name = 'simple_team_list.html'
    queryset = UserView.objects.all()
    context_object_name = 'simple_team'


def delete_page(request, pk):
    UserView.objects.get(pk=pk).delete()
    return redirect('Simpley')


def index(request):
    return render(request, 'update.html')


def update_page(request, pk):
    UserView.objects.filter(pk=pk).update(
        name=request.POST.get("name"),
        category=request.POST.get("category"),
        description=request.POST.get("description"),
        image=request.POST.get("image")
    )
    return redirect('Simpley')


class CustomLoginView(NotLoginRequiredMixin, LoginView):
    template_name = 'login.html'
    next_page = 'index_page'


class RegisterFormView(FormView):
    template_name = 'login.html'
    form_class = RegisterForm
    success_url = reverse_lazy('register_page')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
