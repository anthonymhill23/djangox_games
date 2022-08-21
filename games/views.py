from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "pages/games_home.html"

# Create your views here.
