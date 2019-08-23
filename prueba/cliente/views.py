from django.shortcuts import render
from easy_pdf.views import PDFTemplateView
from .models import Cliente


class FichaPDFViewClientesT(PDFTemplateView):
    template_name = "clientesactivos.html"

    def get_context_data(self, **kwargs):
        clien = Cliente.objects.all()
        return super(FichaPDFViewClientesT, self).get_context_data(
            pagesize="Letter",
            title="Clientes",
            clien=clien,
            **kwargs
        )


class FichaPDFViewClientesF(PDFTemplateView):
    template_name = "clientesinactivos.html"

    def get_context_data(self, **kwargs):
        clien = Cliente.objects.all()
        return super(FichaPDFViewClientesF, self).get_context_data(
            pagesize="Letter",
            title="Clientes",
            clien=clien,
            **kwargs
        )
