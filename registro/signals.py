from django.contrib import admin
from registro.models import Registro
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.response import Response
from django.http import HttpResponse, Http404


@receiver(pre_save, sender=Registro)
def limitar_usuarios(sender, instance, **kwargs):
    
    LIMITE = 10
    if Registro.objects.count() >= LIMITE:
        raise ValidationError(f"❌ Já existem {LIMITE} usuários cadastrados.")

@receiver(post_save, sender=Registro)
def alerta_numero_usuarios(sender, instance, **kwargs):
    
    ALERTA = 5
    if Registro.objects.count() == ALERTA:
        raise Http404()  
        
