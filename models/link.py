from django.db import models

from kernel.models.root import Model
from kernel.utils.upload_to import UploadTo


class Link(Model):
    """
    This model describes a link that appears in miscellaneous links and can
    point to any web page or asset
    """

    title = models.CharField(
        max_length=127,
    )
    url = models.URLField(
        verbose_name='URL',
    )

    description = models.TextField()

    logo = models.ImageField(
        upload_to=UploadTo('links', 'logos'),
        max_length=255,
        blank=True,
        null=True,
    )

    def __str__(self):
        """
        Return the string representation of the object
        :return: the string representation of the object
        """

        title = self.title
        url = self.url

        return f'{title}: {url}'
