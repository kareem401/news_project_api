from rest_framework import viewsets
from django.contrib.auth import get_user_model
from articles.models import Article, Comment
from .serializers import ArticleSerializer, UserSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class ArticleViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Article.objects.all()
	serializer_class = ArticleSerializer

class UserViewSet(viewsets.ModelViewSet):
	queryset = get_user_model().objects.all()
	serializer_class = UserSerializer
 
class CommentViewSet(viewsets.ModelViewSet):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Comment.objects.all()
	serializer_class = CommentSerializer
