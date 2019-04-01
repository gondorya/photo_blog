
from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse, JsonResponse

from blog.models import Post
from blog.serializers import ExampleModelSerializer

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_data(request):
    data = Post.objects.all()
    if request.method == 'GET':
        serializer = ExampleModelSerializer(data, many=True, context={"request": request})
        return JsonResponse(serializer.data, safe=False)