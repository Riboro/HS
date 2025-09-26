from django.test import TestCase
from .models import Registro, Identificador
from .serializer import RegistroSerializer, IdentificadorSerializer, ListarIdentificadorRegistroSerializer

class ListarIdentificadorRegistroSerializerTest(TestCase):
    def setUp(self):
        self.registro = Registro.objects.create(nome="Teste", numero=123)
        self.identificador = Identificador.objects.create(registro=self.registro)

    def test_serializer_fields(self):
        serializer = ListarIdentificadorRegistroSerializer(instance=self.identificador)
        data = serializer.data
        self.assertIn('id', data)
        self.assertIn('registro', data)
        self.assertEqual(data['id'], self.identificador.id)
        self.assertEqual(data['registro'], self.registro.numero)