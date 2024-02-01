from django.contrib import admin
from django.urls import path, include
from .views import home

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('movies/', include('movie.urls')),
    path('celebrity/', include('celebrity.urls') ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# #  admin side titles
# admin.site.index_title = "MRS Admin"
# admin.site.site_header = "MRS Admin"
# admin.site.site_title = "Users"