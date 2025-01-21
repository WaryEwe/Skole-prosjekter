from django.db import models
from django.contrib.auth.models import User
import datetime
class BorrowingModel(models.Model):
    borrowing_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    borrowing_title = models.CharField(max_length=50, null=False)
    borrowing_desc = models.TextField(max_length=70, null=False)
    borrowing_date = models.DateField(auto_now_add=True, null=False)
    borrowing_image = models.ImageField(upload_to='images/', null=False)
    borrowing_stock = models.IntegerField(null=False, default=50)

    def __str__(self):
        return self.borrowing_title
def test():
    return datetime.date.today() + datetime.timedelta(weeks=2)

class RentModel(models.Model):
    borrower = models.ForeignKey(User, on_delete=models.CASCADE, null=False, related_name='borrow_user')
    borrow_material = models.ForeignKey(BorrowingModel, on_delete=models.CASCADE, null=False)
    borrow_date = models.DateField(auto_now_add=True, null=False)
    borrow_expiry = models.DateField(default=test)

    class Meta:
        unique_together = ('borrower', 'borrow_material')
