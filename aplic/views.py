from chartjs.views.lines import BaseLineChartView
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.generic import TemplateView, ListView
from django_weasyprint import WeasyTemplateView
from weasyprint import HTML

from .models import Professor, Curso, Disciplina, Aluno


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['menu_active_item'] = 'nav-item-home'
        context['cursos'] = Curso.objects.order_by('?').all()
        return context


class AboutView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['menu_active_item'] = 'nav-item-about_us'
        return context


class ProfessorListView(ListView):
    template_name = 'teachers.html'
    context_object_name = 'professores'

    def get_context_data(self, **kwargs):
        context = super(ProfessorListView, self).get_context_data(**kwargs)
        context['menu_active_item'] = 'nav-item-teachers'
        return context

    def get_queryset(self):
        return Professor.objects.order_by('nome').all()


class CursoDetailView(ListView):
    template_name = 'course-detail.html'
    paginate_by = 5
    ordering = 'nome'
    context_object_name = 'disciplinas'
    model = Disciplina

    def get_context_data(self, **kwargs):
        context = super(CursoDetailView, self).get_context_data(**kwargs)
        context['curso'] = Curso.objects.filter(pk=self.kwargs['pk']).first()
        return context

    def get_queryset(self, **kwargs):
        return Disciplina.objects.filter(curso_id=self.kwargs['pk']).order_by('nome')


class AlunosChartView(BaseLineChartView):

    def get_labels(self):
        labels = []
        queryset = Curso.objects.order_by('nome')
        for curso in queryset:
            labels.append(curso.nome)
        return labels

    def get_data(self):
        resultado = []
        dados = []
        from django.db.models import Count
        queryset = Curso.objects.order_by('nome').annotate(total=Count('aluno'))
        for linha in queryset:
            dados.append(int(linha.total))
        resultado.append(dados)
        return resultado


class RelatorioAlunosView(WeasyTemplateView):

    def get(self, request, *args, **kwargs):
        alunos = Aluno.objects.order_by('nome').all()
        html_string = render_to_string('relatorio-alunos.html', {'alunos': alunos})
        html = HTML(string=html_string, base_url=request.build_absolute_uri()).write_pdf()
        response = HttpResponse(html, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="relatorio-alunos.pdf"'
        return response
