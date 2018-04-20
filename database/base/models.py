from django.db import models
from django.urls import reverse

# Create your models here.
class Order(models.Model):

    id = models.AutoField(primary_key=True )
    name=models.CharField(max_length=100,null=True)
    type_of_device=models.CharField(max_length=30,null=True)
    serial_n=models.CharField(max_length=30,null=True)
    date_of_issue=models.DateField(null=True, blank=True)
    date_of_done=models.DateField(null=True, blank=True)
    STATUS = (
        ('d', 'Done'),
        ('p', 'Processing'),
    )
    status=models.CharField(max_length=1,choices=STATUS)
    act=models.URLField(null=True)
    outside_osmotr=models.TextField(null=True)
    check_whether_is_working=models.TextField(null=True)
    results_diag=models.TextField(null=True)
    working_was_done=models.TextField(null=True)
    note=models.TextField(null=True)
    responsive_person=models.CharField(max_length=20,null=True)
    #=models.CharField(max_length=10)

    def __str__(self):
            return self.id

    def get_absolute_url(self):
        return reverse('order-detail', args=[str(self.id)])
    def get_absolute_url1(self):
        return reverse('order_update', args=[str(self.id)])
    def get_absolute_url2(self):
        return reverse('order_delete', args=[str(self.id)])
    
