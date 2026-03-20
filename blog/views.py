from django.http import HttpResponse
from .models import Post

def home(request):
    posts = Post.objects.all()
    output = ""

    for post in posts:
        output += f"<h1>{post.title}</h1><p>{post.content}</p>"

    return HttpResponse(output)

