from django.views.generic import CreateView, ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.forms import ModelForm
from helloworld.models import Funcionario
from .forms import InsereFuncionarioForm

class InsereFuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = "__all__"

class IndexView(TemplateView):
    template_name = "website/index.html"

class FuncionarioCreateView(CreateView):
    template_name = "website/cria.html"
    model = Funcionario
    form_class = InsereFuncionarioForm
    success_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "website/exclui-funcionario.html"
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista_funcionarios')

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = '__all__'
    template_name = 'website/atualiza.html'
    context_object_name = 'funcionario'
    success_url = reverse_lazy('website:lista_funcionarios')

class ListaFuncionarios(ListView):
    model = Funcionario
    template_name = 'website/lista.html'
    context_object_name = 'funcionarios'

