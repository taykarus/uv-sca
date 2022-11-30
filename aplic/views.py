from chartjs.views.lines import BaseLineChartView
from django.contrib import messages
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils import translation
from django.views.generic import ListView
from django.views.generic import TemplateView, FormView
from django_weasyprint import WeasyTemplateView
from weasyprint import HTML

from .forms import ContatoForm
from .models import Professor, Curso, Disciplina, Aluno


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        lang = translation.get_language()
        translation.activate(lang)
        context['lang'] = lang
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


class ContatoView(FormView):
    template_name = 'contato.html'
    form_class = ContatoForm
    success_url = reverse_lazy('contato')

    def get_context_data(self, **kwargs):
        context = super(ContatoView, self).get_context_data(**kwargs)
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso', extra_tags='success')
        return super(ContatoView, self).form_valid(form)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Falha ao enviar e-mail', extra_tags='danger')
        return super(ContatoView, self).form_invalid(form)
