
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post
from blog.serializers import PostModelSerializer
from .forms import PostForm

@csrf_exempt
def get_data(request):
    data = Post.objects.all()
    if request.method == 'GET':
        serializer = PostModelSerializer(data, many=True, context={"request": request})
        return JsonResponse(serializer.data, safe=False)

def new_post(request):
    form = PostForm()
    return render(request, 'new_post.html', {'form': form})