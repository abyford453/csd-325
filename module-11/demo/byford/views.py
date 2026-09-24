from django.http import HttpResponse


def index(request):
    """Display a simple greeting for the Module 11 Django assignment."""
    return HttpResponse("Byford says Hello!")