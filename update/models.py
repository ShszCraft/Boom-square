from django.db import models

# Create your models here.


class update(models.Model):
    version = models.CharField(max_length=25)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = (
            ("update_see_article", "url访问权限"),
        )
