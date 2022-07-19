from django.db import models


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    deliverer = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey('OrderStates', models.DO_NOTHING, blank=True, null=True)
    paid_amount = models.IntegerField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    rate = models.IntegerField(blank=True, null=True)
    payment_method = models.IntegerField()
    payment_installment = models.ForeignKey('PaymentInstallments', models.DO_NOTHING, blank=True, null=True)
    cancellation = models.ForeignKey('OrderCancellationReasons', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    customer_rate = models.IntegerField(blank=True, null=True)
    address = models.ForeignKey('Addresses', models.DO_NOTHING, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    unique_id = models.CharField(max_length=255, blank=True, null=True)
    success_indicator = models.CharField(max_length=255, blank=True, null=True)
    scheduled_at = models.DateTimeField(blank=True, null=True)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    referal = models.CharField(max_length=255, blank=True, null=True)
    fawry_ref = models.CharField(max_length=191, blank=True, null=True)
    sub_state = models.ForeignKey('OrderStates', models.DO_NOTHING, blank=True, null=True)
    admin_notes = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=1, blank=True, null=True)
    transaction = models.ForeignKey('Transactions', models.DO_NOTHING, blank=True, null=True)
    phone = models.CharField(max_length=191, blank=True, null=True)
    user_agent = models.CharField(max_length=191, blank=True, null=True)
    admin = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    cancellation_text = models.TextField(blank=True, null=True)
    user_ip = models.CharField(max_length=50)
    affiliate = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    investigation_text = models.CharField(max_length=191, blank=True, null=True)
    erp_id = models.CharField(max_length=191, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'
