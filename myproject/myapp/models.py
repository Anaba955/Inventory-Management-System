# from audioop import reverse
from msilib.schema import File
from django.urls import reverse
from django.core.files.base import ContentFile
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .utils import qrc




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
    last_modified = models.DateTimeField(default=timezone.now)
    created_by = models.ForeignKey(User, default=1, on_delete=models.CASCADE, related_name = 'myapp_features')
    qr_code_image = models.ImageField(upload_to='qr_codes', blank=True)

    def save(self, *args, **kwargs):
        if self.id and not self.qr_code_image:
            qr_url = reverse('box_click', args=[self.id])
            img = qrc(qr_url)
            img_content = ContentFile(img.read())
            self.qr_code_image.save('feature_qr_codes/qr_code.png', img_content, save=False)

        super().save(*args, **kwargs)

            
    def get_absolute_url(self):
        return reverse('box_click', args=[self.id])


    

    def __str__(self):
        return str(self.id)


    
class Items(models.Model):
    id = models.AutoField(primary_key=True)
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

