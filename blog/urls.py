from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path("admin/", admin.site.urls),
    # path("", BlogListView.as_view(), name="blog_views")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)