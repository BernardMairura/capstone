from django.db import models
from authentication.models import User

# Create your models here.


class Expenses(models.Model):

    LEDGER_LINES=[
        ('TRAVEL','TRAVEL'),
        ('RENT','RENT'),
        ('INTERNET','INTERNET'),
        ('AIRTIME','AIRTIME'),
        ('FUEL','FUEL'),
        ('MISCEllANEOUS','MISCEllANEOUS')
    ]

    date=models.DateField(null=False,blank=False)
    ledger=models.CharField(choices=LEDGER_LINES,max_length=255)
    reference= description=models.TextField()
    description=models.TextField()
    amount=models.DecimalField(max_digits=10,decimal_places=2,max_length=255)
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    transaction_date= models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)

    class Meta:
        ordering: ['-modified_date']

    def __str__(self):
        return str(self.user)+'s income'



