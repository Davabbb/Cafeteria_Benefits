from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

@user_passes_test(lambda u: u.is_staff)
def manager_page(request):
    return render(request, 'staff_page.html')

def worker_page(request):
    return render(request, 'regular_page.html')
