from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated

from inforratica.models import OrdemServico, Cliente
from inforratica.serializers import OrdemServicoSerializer, OrdemServicoReadSerializer


class OrdemServicoViewSet(ModelViewSet):
    queryset = OrdemServico.objects.all()
    serializer_class = OrdemServicoSerializer
    queryset = OrdemServico.objects.all().order_by("-data")
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        if self.action == "list":
            return OrdemServicoReadSerializer
        return OrdemServicoSerializer

    # def list(self, request):
    #     # breakpoint()
    #     queryset = OrdemServico.objects.filter(cliente__id=14)
    #     serializer = OrdemServicoReadSerializer(queryset, many=True)
    #     return Response(serializer.data)
