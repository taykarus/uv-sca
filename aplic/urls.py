from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CursoViewSet
from .views import IndexView, AboutView, ProfessorListView, CursoDetailView, AlunosChartView, RelatorioAlunosView, \
    ContatoView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('sobre/', AboutView.as_view(), name='about-us'),
    path('professores/', ProfessorListView.as_view(), name='professor-list'),
    path('cursos/<int:pk>/', CursoDetailView.as_view(), name='curso-detail'),
    path('alunos/grafico/', AlunosChartView.as_view(), name='alunos-grafico'),
    path('relatorio-alunos/', RelatorioAlunosView.as_view(), name='relatorio-alunos'),
    path('contato/', ContatoView.as_view(), name='contato'),
]

router = SimpleRouter()
router.register('cursos', CursoViewSet)
