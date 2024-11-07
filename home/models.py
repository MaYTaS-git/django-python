from django.db import models


# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField(max_length=120)
    phone = models.CharField(max_length=13)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

    def is_valid(self):
        # name check
        if len(self.name) <= 1:
            return False

        # phone number check
        elif len(str(self.phone)) < 10 or len(str(self.phone)) > 13:
            print(self.phone)
            return False


        # desc check
        elif len(self.desc) < 3:
            print('error here')
            return False

        else:
            return True
