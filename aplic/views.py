from django.views.generic import TemplateView, ListView, DetailView
from .models import Professor, Curso, Disciplina


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
