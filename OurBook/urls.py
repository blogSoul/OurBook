from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ckeditor_uploader import views as views_ckeditor
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('main/', include('main.urls')),
    path('books/', include('bookstore.urls')),
    path('solutions/', include('solutions.urls')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('upload/', login_required(views_ckeditor.upload), name='ckeditor_upload'),
    path('browse/', never_cache(login_required(views_ckeditor.browse)), name='ckeditor_browse'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
