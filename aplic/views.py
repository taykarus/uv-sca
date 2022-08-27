from django.views.generic import TemplateView
from .models import Professor, Curso


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['menu_active_item'] = 'nav-item-home'
        context['cursos'] = Curso.objects.order_by('?').all()
        return context


class SobreView(TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super(SobreView, self).get_context_data(**kwargs)
        context['menu_active_item'] = 'nav-item-about_us'
        return context


class ProfessoresView(TemplateView):
    template_name = 'teachers.html'

    def get_context_data(self, **kwargs):
        context = super(ProfessoresView, self).get_context_data(**kwargs)
        context['professores'] = Professor.objects.order_by('nome').all()
        context['menu_active_item'] = 'nav-item-professores'
        return context
