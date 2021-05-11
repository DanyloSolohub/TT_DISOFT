from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import PerformerSerializer
from .models import PerformerModel


class ListView(ListAPIView):
    queryset = PerformerModel.objects.all()
    serializer_class = PerformerSerializer


class ReadUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PerformerSerializer
    queryset = PerformerModel.objects.all()
