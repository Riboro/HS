from rest_framework import viewsets, generics
from registro.models import Registro
from .serializer import RegistroSerializer, ListarIdentificadorRegistroSerializer
from .models import Registro



class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
            


class ListarIdentificadorRegistroViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Registro.objects.filter(numero=self.kwargs['registro_numero'])
        return queryset
    serializer_class = ListarIdentificadorRegistroSerializer