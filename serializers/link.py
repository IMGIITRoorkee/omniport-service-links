from links.models import Link
from formula_one.serializers.base import ModelSerializer


class LinkSerializer(ModelSerializer):
    """
    Serializer for Link objects
    """

    class Meta:
        """
        Meta class for LinkSerializer
        """

        model = Link
        exclude = [
            'datetime_created',
            'datetime_modified',
        ]
