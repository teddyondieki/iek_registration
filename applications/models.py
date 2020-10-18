from django.contrib.auth import get_user_model
from django.db import models
from django.db.models import SET_NULL, CASCADE


class ApplicationCategory(models.Model):
    name = models.CharField(max_length=128)
    account_category = models.OneToOneField('accounts.AccountCategory', on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name


class ApplicationQuestion(models.Model):
    category = models.ForeignKey( ApplicationCategory, related_name='questions', on_delete=CASCADE)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, null=True, blank=True)
    length = models.IntegerField()

    # TODO: Add type later on and give more options

    def save(self, *args, **kwargs):
        if self.pk:
            is_new = False
        else:
            is_new = True

        super(ApplicationQuestion, self).save(*args, **kwargs)

        if True:
            for application in self.category.applications.all():
                answer = ApplicationAnswer()
                answer.question = self
                answer.application = application
                answer.save()

    def __str__(self):
        return '{}: {}'.format(self.category.name, self.name)

class Application(models.Model):
    user = models.OneToOneField('accounts.CustomAccount', on_delete=CASCADE, related_name='application')
    category = models.ForeignKey(ApplicationCategory, on_delete=SET_NULL, null=True, related_name='applications')
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.category.name


class ApplicationAnswer(models.Model):
    application = models.ForeignKey(Application, on_delete=CASCADE, related_name='answers')
    question = models.ForeignKey(ApplicationQuestion, on_delete=CASCADE, related_name='answers')
    content = models.TextField(null=True)

    def __str__(self):
        return '{}: {}'.format(self.question.name, self.content)
