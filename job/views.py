from django.shortcuts import render
from .models import job
from django.core.paginator import Paginator

from .form import applyform, jobForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


# Create your views here.
@login_required
def job_list(request):
    job_list=job.objects.all()
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs

    paginator=Paginator(job_list, 4)
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)





    context={'jobs':page_obj, 'myfilter': myfilter}
    return render(request, 'job/job_list.html',context)




def job_detail(request, id):
    job_detail=job.objects.get(id=id)

    if request.method=='POST':
        form=applyform(request.POST, request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.jobi=job_detail
            myform.save()
        
    else:
        form=applyform()
    context={'job': job_detail, 'form':form}
    return render(request,'job/job_detail.html', context)

def add_job(request):
    if request.method=='POST':
        form=jobForm(request.POST,request.FILES)
        if form.is_valid():
            myform=form.save(commit=False)
            myform.owner=request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form=jobForm()


    return render(request,'job/add_job.html',{'form':form})
   
