from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator

# regex to match a comma separated list of three floats
size_validator = RegexValidator(regex=r'^(\d*\.\d+|\d+),(\d*\.\d+|\d+),(\d*\.\d+|\d+)$',
                                message='Enter L,W,H as numbers in meters')

# regex for validating phone numbers
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                             message="Phone number must be entered in the format '+999999999' without separators.")


class Manufacturer(models.Model):
    """
    These are the manufacturers of the items in our inventory
    """
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=15, validators=[phone_regex], blank=True)

    class Meta:
        app_label = 'inventory'

    def __unicode__(self):
        """
        This method just returns a friendly representation of a manufacturer
        """
        return '{}'.format(self.name)


class InventoryItem(models.Model):
    """
    A model of objects that can be stored in inventory
    """
    name = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, null=False)
    description = models.CharField(max_length=800)
    size = models.CharField(max_length=32, null=True, validators=[size_validator])
    weight = models.FloatField(null=True)
    unit_of_issue = models.CharField(max_length=8, default='EACH')
    quantity = models.IntegerField(null=False)
    # defaults need to either be immutable, or a callable
    # by using timezone.now we're storing in UTC which can be converted
    # to local time on the client side
    last_changed = models.DateTimeField(default=timezone.now)

    class Meta:
        app_label = 'inventory'

    def __unicode__(self):
        """
        This method just returns a friendly representation of an inventory item
        """
        return '{0} from {1}. Qty: {2} {3}'.format(self.name, self.manufacturer, self.quantity, self.unit_of_issue)
