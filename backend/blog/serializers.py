from rest_framework import serializers
from blog.models import Post

class ExampleModelSerializer(serializers.ModelSerializer):
    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date', 'author', 'photo_url')

    def get_photo_url(self, post):
        request = self.context.get('request')
        photo_url = post.image.url
        return request.build_absolute_uri(photo_url)