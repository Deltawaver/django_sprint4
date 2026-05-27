from django.shortcuts import render
from django.views.generic import TemplateView


class AboutView(TemplateView):
    """Страница 'О проекте'."""
    template_name = 'pages/about.html'


class RulesView(TemplateView):
    """Страница с правилами."""
    template_name = 'pages/rules.html'


def page_not_found(request, exception):
    """Обработчик 404 ошибки."""
    return render(request, 'pages/404.html', status=404)


def csrf_failure(request, reason=''):
    """Обработчик 403 CSRF ошибки."""
    return render(request, 'pages/403csrf.html', status=403)


def permission_denied(request, exception):
    """Обработчик 403 ошибки доступа."""
    return render(request, 'pages/403csrf.html', status=403)


def server_error(request):
    """Обработчик 500 ошибки сервера."""
    return render(request, 'pages/500.html', status=500)