from django.urls import path, include
from rest_framework import routers

from links.views.links import LinkViewSet

router = routers.SimpleRouter()
router.register('link', LinkViewSet, base_name='link')

urlpatterns = [
    path('', include(router.urls)),
]
