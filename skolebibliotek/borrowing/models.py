from django.db import models
from django.contrib.auth.models import User


class BorrowingModel(models.Model):
    borrower_user_id = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='user_borrower')
    borrowing_title = models.CharField(max_length=50, null=False)
    borrowing_desc = models.TextField(max_length=70, null=False)
    borrowing_date = models.DateField(auto_now_add=True)
    borrowing_image = models.ImageField(upload_to='images/', null=False)
    def __str__(self):
        return self.borrowing_title

class BorrowModel:
    borrower = models.ForeignKey(User, on_delete=models.CASCADE)
    borrower_item = models.ForeignKey(BorrowingModel, on_delete=models.CASCADE)
    borrower_date = models.DateField(auto_now_add=True)
