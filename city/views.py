from rest_framework import viewsets, status
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from django.db.models import Avg
from .models import City, CityTemperature
from .serializers import CitySerializer, TemperatureSerializer


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    @action(detail=True, methods=['post'], url_path='setTemperature')
    def set_temperature(self, request, pk=None):
        city = self.get_object()
        serializer = TemperatureSerializer(data=request.data)
        if serializer.is_valid():
            CityTemperature.objects.create(city=city, value=serializer.validated_data['value'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_stats(request):
    city_id = request.query_params.get('city_id')
    temps = CityTemperature.objects.all()
    if city_id:
        temps = temps.filter(city_id=city_id)
    avg_temp = temps.aggregate(average=Avg('value'))['average']
    return Response({'average': avg_temp})
