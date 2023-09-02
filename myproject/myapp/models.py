from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver



class Racks(models.Model):
    Rid = models.IntegerField(primary_key=True)
    Rname = models.CharField(max_length=10, null=False, blank=False)
    Rqty = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.Rid)


class features(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    Qty = models.DecimalField(decimal_places=2, max_digits=10)
    rack_id = models.ForeignKey(Racks, on_delete=models.CASCADE, default=1, to_field='Rid')
    # qrcode = models.ImageField()
    last_modified = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


    
class Items(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    Qty = models.IntegerField(default=0)
    box_id = models.ForeignKey(features, on_delete=models.CASCADE, default = 8,to_field='id')
    # added_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    


@receiver(post_save, sender=features)
def update_rack_qty_on_feature_save(sender, instance, created, **kwargs):
    """
    Signal receiver to update Rqty attribute of the related Rack when a Feature is saved.
    """
    if created:
        instance.rack_id.Rqty += 1
    else:
        # Feature was updated, no need to change Rqty
        return

    # Save the Rack instance with the updated Rqty
    instance.rack_id.save()


@receiver(post_delete, sender=features)
def update_rack_qty_on_feature_delete(sender, instance, **kwargs):
    """
    Signal receiver to update Rqty attribute of the related Rack when a Feature is deleted.
    """
    instance.rack_id.Rqty -= 1
    instance.rack_id.save()

