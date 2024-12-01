from django.db import models
from django.conf import settings


class Mortgage(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="mortgages"
    )
    lender_name = models.CharField(max_length=100)
    interest_rate = models.FloatField()
    max_amount = models.FloatField()
    loan_type = models.CharField(max_length=100)
    min_down_payment = models.FloatField()
    loan_term = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.lender_name
