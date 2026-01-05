from django.urls import path
from .views import IndexView
from .views import FuncionarioCreateView, ListaFuncionarios, FuncionarioUpdateView
from .views import ListaFuncionarios
from .views import FuncionarioDeleteView

app_name = 'website'

urlpatterns = [
    path('funcionarios/', ListaFuncionarios.as_view(), name='lista_funcionarios'),
    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(), name='cadastra_funcionario'),
    path('funcionarios/editar/<int:pk>/', FuncionarioUpdateView.as_view(), name='atualiza_funcionario'),
    path('funcionario/excluir/<int:pk>/', FuncionarioDeleteView.as_view(), name='deleta_funcionario'),
    path("", IndexView.as_view(), name="index"),

]
