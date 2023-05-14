from django.shortcuts import render
from .tasks import mock_task, get_result_by_id
from django.conf import settings


def index(request):
    msg = None
    if settings.CURRENT_TASK_ID is None:
        tsk = mock_task.delay(5)
        settings.CURRENT_TASK_ID = tsk.id
    else:
        msg = get_result_by_id(settings.CURRENT_TASK_ID)
        if msg:
            settings.CURRENT_TASK_ID = None
    return render(request, 'index.html', {"msg": msg})
