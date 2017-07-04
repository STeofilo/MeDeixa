from django.shortcuts import render
from .models import Activity


def user_index(request):
    a = Activity.objects.all()
    print(a)
    return render(request, 'core/user_index.html', {'activities': a})
