from django.views.generic import TemplateView


class MascotasView(TemplateView):
    template_name = "index.html"

class ConsumirAPIView(TemplateView):
    template_name = "consumirAPI.html"

class Form1View(TemplateView):
    template_name = "form1.html"

class NosotrosView(TemplateView):
    template_name = "nosotros.html"

class NoticiasView(TemplateView):
    template_name = "noticias.html"

