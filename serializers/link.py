from links.models import Link
from kernel.serializers.root import ModelSerializer


class LinkSerializer(ModelSerializer):
    """
    Serializer for Link objects
    """

    class Meta:
        """
        Meta class for LinkSerializer
        """

        model = Link
        fields = [
            'title',
            'url',
            'description',
            'logo',
        ]
