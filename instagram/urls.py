from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'instagram'

router = DefaultRouter()
router.register(r'Post', views.PostViewSet) # 2개의 url
# router.urls


urlpatterns = [
    # path('public/', views.public_post_list), 
    path('', include(router.urls)),
]
