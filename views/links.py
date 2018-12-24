from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from links.models import Link
from links.serializers.link import LinkSerializer


class LinkViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Return the set of important links defined on the portal
    """

    permission_classes = [IsAuthenticated, ]
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    pagination_class = None
