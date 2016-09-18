from django.conf.urls import url
from . import views
urlpatterns = [
        url(r'^register$', views.signup, name='register'),
        url(r'^logout$', views.logout_view, name='logout'),
        url(r'^$', views.home, name='home'),
]
