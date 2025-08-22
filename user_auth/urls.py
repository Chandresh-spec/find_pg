
from django.urls import path,include
from . import views


urlpatterns = [
    path('register/',views.step_form,name='step_form'),
    # path('login/',views.login_view,name='login'),
    # path('logout/',views.logout_view,name='logout')

   
]
