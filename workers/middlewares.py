from django.shortcuts import redirect


class ManagerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        user = request.user
        if user.is_authenticated:
            if user.is_staff:
                return redirect('manager_page')
            else:
                return redirect('worker_page')
        response = self.get_response(request)
        return response
    