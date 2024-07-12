from django.views import generic

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'base.html'