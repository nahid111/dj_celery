from django.shortcuts import render
from .tasks import mock_task


def index(request):
    res = mock_task.delay()
    print(res.id)
    return render(request, 'index.html')
