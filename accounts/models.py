from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import SET_NULL, CASCADE

from applications.models import Application, ApplicationAnswer


class AccountCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class CustomAccount(AbstractUser):
    category = models.ForeignKey(AccountCategory, on_delete=SET_NULL, null=True)
    is_approved = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(CustomAccount, self).save(*args, **kwargs)

        if not self.pk and self.category:
            application = Application()
            application.user = self
            application.category = self.category.applicationcategory
            application.save()

            for question in application.category.questions.all():
                answer = ApplicationAnswer()
                answer.question = question
                answer.application = application
                answer.save()

