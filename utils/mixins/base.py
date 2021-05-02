from django.db import models

class BaseMixin(models.Model):
  class Meta:
    abstract = True
  
  active = models.BooleanField(default=True)
  created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de criação')
  updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de atualização')