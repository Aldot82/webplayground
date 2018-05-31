from django.shortcuts import render
from django.views.generic.base import TemplateView

class HomeView(TemplateView):
    template_name = 'core/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi super web playground'
        return context

    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'title':'Mi super web playground.Segunda parte.'})

class SampleView(TemplateView):
    template_name = 'core/sample.html'

    """def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context"""