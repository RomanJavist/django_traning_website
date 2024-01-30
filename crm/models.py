from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    Status_name = models.CharField(max_length=200, verbose_name='Status name')

    def __str__(self):
        return self.Status_name
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_phone = models.CharField(max_length=200, verbose_name='Phone')
    order_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        return self.order_name

    # class Meta:
    #     verbose_name = 'Beetle'
    #     verbose_name_plural = 'Beetles'

class ComentCrm(models.Model):
    coment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Application')
    coment_text = models.TextField(verbose_name='Comment text')
    coment_dt = models.DateTimeField(auto_now=True, verbose_name='Creation date')

    def __str__(self):
        return self.coment_text
