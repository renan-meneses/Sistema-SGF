from django.conf.urls import url
from . import views

app_name = 'rh'
urlpatterns = [
    #Lista de funcionarios
url(r'gerarlancamento/$', views.CadastroColaboradoresView.as_view(),name='colaboradoresview'),
    #Adicionar colaboradores
    #Remover Colaboradores
    #Editar coloboradores

]