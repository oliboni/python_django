
from django.contrib       import admin
from django.urls          import path
from core                 import views
from django.views.generic import RedirectView
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from .                    import settings

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('pet/all', views.list_all_pets),
    path('pet/user', views.list_user_pets),
    path('pet/detail/<id>/', views.pat_datail),
    path('login/' , views.login_user),
    path('login/submit', views.submit_login),
    path('', RedirectView.as_view(url='pet/all')),
    path('logout/', views.logout_user),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root =  settings.MEDIA_ROOT)
