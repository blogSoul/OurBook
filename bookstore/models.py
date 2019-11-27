from django.db import models
from accounts.models import MyUser

class UserBook(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    link = models.URLField()

    author = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

    publisher = models.CharField(max_length=200)
    pub_date = models.CharField(max_length=200)
    isbn = models.CharField(max_length=200, primary_key=True)

    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title


class Product(models.Model):
    
    exchange_type = (
        ("양도", "양도"),
        ("대여", "대여"),
        ("판매", "판매")
    )

    book_state = (
        ("unavailable", "unavailable"),
        ("available", "available"),
    )

    exchange_method = (
        ("일반거래", "일반거래"),
        ("안심거래", "안심거래"),
    )

    user = models.ForeignKey(MyUser, on_delete = models.CASCADE, null=True)
    book = models.ForeignKey(UserBook, on_delete = models.CASCADE, null=True)
    note = models.CharField(max_length=255)
    ex_type = models.CharField(max_length=10, choices=exchange_type, default="양도")               # 대여, 양도, 판대
    state = models.CharField(max_length=10, choices=book_state, default="unavailable")                  # 판매 완료
    exc_method = models.CharField(max_length=10, choices=exchange_method, default="일반거래")             # 안심거래, 일반거래 
    price = models.CharField(max_length=100, blank=True)