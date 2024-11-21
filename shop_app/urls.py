from django.urls import path
from . import views
from user.views import register_view, login_view, logout_view


urlpatterns = [
    path('', views.home_page, name='home'),
    path('category/<int:pk>', views.category_page),
    path('product/<int:pk>', views.product_page),
    path('registration/', register_view),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('about/', views.about, name='about')
]
