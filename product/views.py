from django.views import generic

#Nabil Moiun - youtube channel for this project

# Create your views here.
class Home(generic.TemplateView):
    template_name = 'home.html'

class PrdocutDetail(generic.TemplateView):
    template_name = 'product/product-details.html'