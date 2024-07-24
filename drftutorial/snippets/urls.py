from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,   
)


from snippets import views

# Create a router and register our ViewSets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet, basename='snippet')
router.register(r'users', views.UserViewSet, basename='user')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
    path('authurl/', views.AuthView.as_view(), name='example-view'),
    path('customauth/', views.CustomAuthView.as_view(), name='customauth-view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/update/', views.BookListUpdateView.as_view(), name='book-list-update'),
    path('userprofile/<int:pk>/', views.UserProfileDetail.as_view(), name='userprofile-detail'),
    path('artist/<int:pk>/', views.ArtistDetail.as_view(), name='artist-detail'),



]