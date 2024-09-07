from django.views import View
from django.core.mail import send_mail
from django.shortcuts import render ,redirect

from .models import *
from .forms import *
# Create your views here.



class IndexView(View):

    form_class = NewLaterForm
    template_name = 'weblog/index.html'

    def get(self , request):
        skills = Skill.objects.all()
        sample_works = SampleWork.objects.all()
        blogs = Blog.objects.order_by('-id')
        return render(request,self.template_name,{
            'skills':skills,
            'sample_works':sample_works,
            'blogs':blogs,
        })
    
    def post(self , request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            Notification.objects.create(email = cd['email'])
            return redirect('index')
        return render(request,self.template_name,{'form':form})


class ContactView(View):

    form_class = ContactForm
    template_name = 'weblog/contact.html'

    def get(self , request ):
        return render(request,self.template_name)
    
    def post(self , request):
        form = self.form_class(request.POST)

        if form.is_valid():
            cd =form.cleaned_data
            msg = "You received an email \n Email : {} \n Message: {}".format(cd['email'] , cd['message'])
            send_mail('' , msg , cd['email'] ,['alighalenoei8383@gmail.com'] , fail_silently=False)
            return redirect('index')
        return render(request,self.template_name,{'form':form})
    

class AbutView(View):

    template_name = 'weblog/abut.html'

    def get(self , request):
        return render(request,self.template_name)
    

class DetailBlogView(View):

    template_name = 'weblog/detail_blog.html'

    def get(self , request , blog_id):
        blog = Blog.objects.get(id = blog_id)
        return render(request,self.template_name,{'blog':blog})