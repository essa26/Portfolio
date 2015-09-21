from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response

# Create your views here.
from django.template import RequestContext
from main.forms import SendEmail
from main.models import Project, Skill, WorkExperience, Education
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt


def home(request):

    context = {}

    form = SendEmail()

    jobs = WorkExperience.objects.all()

    skills = Skill.objects.all()

    for skill in skills:
        print skill.name
        print skill.skillimage_set.all().first().image.url

    studies = Education.objects.all()

    context['form'] = form

    context['skills'] = skills

    context['jobs'] = jobs

    context['studies'] = studies

    return render_to_response('home.html', context, context_instance=RequestContext(request))

@csrf_exempt
def send_email_view(request):

    if request.method == 'POST':
        form = SendEmail(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            message = request.POST['message']

            fullemail = """%s, %s, %s:
%s""" % (name, email, phone_number, message)

            try:
                send_mail('Contact', fullemail, email, ['ESSAIBRAHIMINFO@GMAIL.COM'])

                return HttpResponseRedirect('/')
            except:
              return HttpResponseRedirect('/')
        else:
          return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


#
# def project_list(request):
#
#     context = {}
#
#     projects = Project.objects.all()
#
#     context['projects'] = projects
#
#     return render_to_response(project_list.html, context, context_instance=RequestContext(request))
#
#
# def skill_list(request):
#
#     context = {}
#
#     skills = Skill.objects.all()
#
#     context['skills'] = skills
#
#     return render_to_response(skill_list.html, context, context_instance=RequestContext(request))
