from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('person', views.PersonViewSet, basename='Person')

router.register('products', views.ProductViewSet, basename='Product')

router.register('cart', views.CartViewSet, basename='Cart')


urlpatterns = [
    path('', views.index, name='IndexPage'),
    path('api/login/', views.login, name='Login'),
    path('api/register/', views.register, name='Register'),

    path('api/faqs/<str:pk>/', views.get_faqs, name='FAQs'),
    path('api/profile/', views.get_profile, name='Profile'),


    path('api/', include(router.urls))
]