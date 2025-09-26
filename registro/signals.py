from django.contrib import admin
from registro.models import Registro
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.core.exceptions import ValidationError


@receiver(pre_save, sender=Registro)
def limitar_usuarios(sender, instance, **kwargs):
    LIMITE = 3
    if not instance.pk and Registro.objects.count() >= LIMITE:
        raise ValidationError(f"❌ Já existem {LIMITE} usuários cadastrados.")