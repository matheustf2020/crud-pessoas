from django.urls import path
from . import views


urlpatterns = [
    path('criar_pessoa/', views.criar_pessoa, name='criar_pessoa'),
    path('listar_pessoas/', views.listar_pessoas, name='listar_pessoas'),
    path('editar_pessoa/<int:id>/', views.editar_pessoa, name='editar_pessoa'),
    path('deletar_pessoa/<int:id>/', views.deletar_pessoa, name='deletar_pessoa'),
    path('listar_projetos/', views.listar_projetos, name='listar_projetos'),
    path('criar_projeto/', views.criar_projeto, name='criar_projeto'),
    path('deletar_projeto/<int:id>/', views.deletar_projeto, name='deletar_projeto'),
    path('vincular_pessoas/<int:id>/', views.vincular_pessoas, name='vincular_pessoas'),
]
