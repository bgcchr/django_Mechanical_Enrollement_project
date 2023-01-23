from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Enrollment import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.HomeView.as_view(),name='home'),



]
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)