from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("common/", include("petstagram.common.urls")),
    path("", include("petstagram.accounts.urls")),
    path("pets/", include("petstagram.pets.urls")),
    path("photos/", include("petstagram.photos.urls")),
    path("adoption/", include("petstagram.adoption.urls")),
    path("events/", include("petstagram.events.urls")),
    path("comments/", include("petstagram.comments.urls")),
    path("faq/", include("petstagram.faq.urls")),
]
handler404 = 'petstagram.accounts.views.error_404_view'
handler500 = 'petstagram.accounts.views.error_500_view'
# handler403 = 'petstagram.accounts.views.error_403_view'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
