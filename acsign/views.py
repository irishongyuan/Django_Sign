from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.utils import timezone
from django.urls import reverse
from .models import Sign, Activity

# Create your views here.
def index(request):
    latest_activity_list = Activity.objects.order_by('pub_date')[:2]
    template = loader.get_template('acsign/index.html')
    context = {'latest_activity_list':latest_activity_list,}
    return HttpResponse(template.render(context, request))

def detail(request, activity_id):
    try:
        activity = Activity.objects.get(pk=activity_id)
    except Activity.DoesNotExist:
        raise Http404("Activity does not exit")
    return render(request, 'acsign/detail.html', {'activity':activity})

def results(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    return render(request, 'acsign/results.html', {'activity':activity})

def sign(request, activity_id):
    activity = get_object_or_404(Activity, pk=activity_id)
    sign_name = request.POST['sign_name']

    #防止重复签到
    for sign_object in activity.sign_set.all():
        if sign_name == sign_object.sign_name:
            return render(request, 'acsign/detail.html', {
                'activity': activity,
                'error_message': "You have signed, don't repeat sign.",
            })
    #防止签到数据为空
    if "" == sign_name or "InputYourName" == sign_name :
        return render(request, 'acsign/detail.html', {
            'activity': activity,
            'error_message': "You didn't sign by your name.",
        })
    else:
        activity.sign_set.create(sign_name=sign_name, sign_date=timezone.now())
        activity.save()

    #返回签到成功后页面，即调用results函数
    return HttpResponseRedirect(reverse('acsign:results', args=(activity_id,)))
