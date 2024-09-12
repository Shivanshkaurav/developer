from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', recipe, name='recipe'),
    path('delete_recipe/<int:id>/', delete_recipe, name='delete_recipe'),
    path('search_recipe/', search_recipe, name='search_recipe'),
    path('edit_recipe/<int:id>/', update_recipe, name='edit_recipe')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)