from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post
# from marketing.models import Signup

def index(request):
    queryset = Post.objects.all()
    latest_col = Post.objects.order_by('-timestamp')[0:6]

    paginator = Paginator(queryset, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    # if request.method=="POST":
    #     email = request.POST["email"]
    #     new_signup = Signup()
    #     new_signup.email = email
    #     new_signup.save()

    context = {
        'queryset': paginated_queryset,
        'page_request_var': page_request_var,
        'latest_col': latest_col,

    }
    return render(request, 'pages/index.html', context)

def about(request):
    latest_col = Post.objects.order_by('-timestamp')[0:6]
    context = {
        'latest_col': latest_col
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    latest_col = Post.objects.order_by('-timestamp')[0:6]
    context = {
        'latest_col': latest_col
    }
    return render(request, 'pages/contact.html', context)

def post_details(request, slug):
    # return HttpResponse(slug)
    latest_col = Post.objects.order_by('-timestamp')[0:6]
    post_content = Post.objects.get(slug=slug)
    # post_content = get_object_or_404(Post, pk=slug)
    context = {
        'post_content': post_content,
        'latest_col': latest_col
    }
    return render(request, 'pages/post_detail.html', context)
