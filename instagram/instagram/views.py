from django.views import generic

from braces import views


class HomePageView(views.AnonymousRequiredMixin,
                   generic.TemplateView):
    template_name = 'home.html'
