from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Station
from .serializers import StationSerializer

@api_view(['POST'])
def create_station(request):
    print("---------------------",request)
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_all_stations(request):
    print("********************")
    stations = Station.objects.all()
    serializer = StationSerializer(stations, many=True)
    return Response(serializer.data)