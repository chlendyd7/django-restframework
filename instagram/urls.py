from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'instagram'

router = DefaultRouter()
router.register(r'post', views.PostViewSet) # 2개의 url
# router.urls


urlpatterns = [
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
    # path('public/', views.public_post_list), 
    path('', include(router.urls)),
]
