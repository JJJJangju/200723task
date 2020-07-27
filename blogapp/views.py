from django.shortcuts import render,get_object_or_404,redirect
from .models import Blogapp
from django.utils import timezone

def main(request):
    blog_all = Blogapp.objects.all().order_by('-id') #쿼리셋, 객체목록 가져오기
    # blog_all = blog.all()
    return render(request,'main.html',{'blogs':blog_all})


def detail(request,blog_id):
    blog=get_object_or_404(Blogapp,pk=blog_id)
    return render(request,'detail.html',{'blog':blog})

def new(request): # new 화면 띄우기 
    return render(request,'new.html')

def create(request):
    blog = Blogapp()
    blog.user = request.user
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))

def renew(request,blog_id):
    blog_r=get_object_or_404(Blogapp,pk=blog_id)
    return render(request,'renew.html',{'blog':blog_r})


def update(request,blog_id):
    blog = get_object_or_404(Blogapp,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save()
    return redirect('/detail/' + str(blog.id))


def delete(request,blog_id):
    blog_d=get_object_or_404(Blogapp,pk=blog_id)
    blog_d.delete()
    return redirect('/')