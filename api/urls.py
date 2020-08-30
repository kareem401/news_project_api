from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ArticleViewSet, UserViewSet, CommentViewSet


router = SimpleRouter()
router.register("comments", CommentViewSet, basename="comments")
router.register("users", UserViewSet, basename="users")
router.register("", ArticleViewSet, basename="Articles")
urlpatterns = router.urls
