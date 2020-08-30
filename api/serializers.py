from rest_framework import serializers
from articles.models import Article, Comment
from users.models import CustomUser

class ArticleSerializer(serializers.ModelSerializer):
	class Meta:
		model = Article
		fields = ("id","title", "body", "date","author")

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ("id", "article" , "comment", "author")

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomUser
		fields = ("id", "username", "email", "password","age")