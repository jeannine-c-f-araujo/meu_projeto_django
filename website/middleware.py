from django.http import HttpResponse

class MiddlewareSimples:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_exception(self, request, exception):
        print("Exceção capturada pelo middleware:", exception)
        return None   

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Antes de executar a View:", view_func.__name__)
        return None

    def __call__(self, request):
        print("Antes da View")
        response = self.get_response(request)
        print("Depois da View")
        return response
