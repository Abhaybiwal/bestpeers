from snippets.models import Snippet
from snippets.serializers import SnippetSerializer,UserSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import renderers,viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework import authentication,status
from rest_framework import exceptions
from .authentication import CustomAuthentication
from django.contrib.auth import authenticate
from .models import Book,UserProfile,Artist
from .serializers import BookSerializer,UserProfileSerializer,ArtistSerializer


class UserProfileDetail(generics.RetrieveAPIView):
    # authentication_classes=[CustomAuthentication]
    # permission_classes=[IsAuthenticated]
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class ArtistDetail(generics.RetrieveAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('snippet-list', request=request, format=format)
    })



class CustomAuthView(APIView):

    def get(self, request):
        return Response({"message": "Hello, authenticated user!"}, status=status.HTTP_200_OK)

class AuthView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        token, created = Token.objects.get_or_create(user=request.user)
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
            'token': token.key,
        }
        return Response(content)
    

class BookListView(APIView):
    
    def get(self,request):
        books = Book.objects.all()
        serializer = BookSerializer(books,many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data, many=True)
        if serializer.is_valid():
            books = serializer.save()  # Calls the custom create method
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        try:
            book_instances = Book.objects.all()
            serializer = BookSerializer(book_instances, data=request.data, many=True)
            if serializer.is_valid():
                serializer.save()  
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class BookListUpdateView(APIView):
    authentication_classes  = []
    permission_classes = []
    def put(self, request, *args, **kwargs):
        book_instances = Book.objects.all()
        serializer = BookSerializer(book_instances, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()  
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Next we're going to replace the SnippetList, SnippetDetail and SnippetHighlight view classes
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

# we are replacing this with Viewset(UserViewSet)
# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = [renderers.StaticHTMLRenderer]

#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)
    
class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)