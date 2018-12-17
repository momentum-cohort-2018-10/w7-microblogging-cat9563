from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import Response 
from rest_framework import reverse
from rest_framework import renderers
from rest_framework.response import Response

class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })

class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.object.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, requests, *args, **kwargs):
        snippet = self.get_objects()
        return Response(snippet.highlighted)

