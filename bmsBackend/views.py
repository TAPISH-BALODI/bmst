from datetime import timezone
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Journey, Station
from .serializers import JourneySerializer, StationSerializer
from django.utils import timezone
from django.db.models import Avg

@api_view(['POST'])
def create_station(request):
    serializer = StationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_all_stations(request):
    stations = Station.objects.all()
    serializer = StationSerializer(stations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_journey(request):
    serializer = JourneySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update_journey(request,id):
    try:
        journey = Journey.objects.get(pk=id)
        print(journey)
        serializer = JourneySerializer(journey, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Journey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    


@api_view(['PUT'])
def update_station(request, id):
    try:
        station = Station.objects.get(pk=id)
        
        updated_data = {}
        if 'onboard_frequency' in request.data:
            updated_data['onboard_frequency'] = request.data['onboard_frequency']
        if 'offboard_frequency' in request.data:
            updated_data['offboard_frequency'] = request.data['offboard_frequency']
        
        serializer = StationSerializer(station, data=updated_data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Station.DoesNotExist:
        return Response({"error": "Station with the specified ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_journey(request,id):
    try:
        journey = Journey.objects.get(pk=id)
        serializer = JourneySerializer(journey)
        return Response(serializer.data)
    except Journey.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

@api_view(['PUT'])
def end_journey(request, id):
    try:
        journey = Journey.objects.get(pk=id)
        # Update only the end_time attribute
        journey.end_time = timezone.now()

        duration = journey.end_time - journey.start_time
        total_seconds = duration.total_seconds()
        hours = int(total_seconds // 3600)
        minutes = int((total_seconds % 3600) // 60)
        journey.total_duration = f"{hours} hours, {minutes} minutes"

        journey.save()
        serializer = JourneySerializer(journey)

        return Response({"message": "Journey ended successfully", "data": serializer.data}, status=status.HTTP_200_OK)
    except Journey.DoesNotExist:
        return Response({"error": "Journey with the specified ID does not exist."}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

@api_view(['GET'])
def get_journey_analytics(request):
    journeys = Journey.objects.all()
    serializer = JourneySerializer(journeys, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def overall_analytics(request):
    # Average total_duration, total_passengers, available_seats
    
    avg_duration = Journey.objects.aggregate(avg_duration=Avg('total_duration'))
    avg_passengers = Journey.objects.aggregate(avg_passengers=Avg('total_passengers'))
    avg_seats = Journey.objects.aggregate(avg_seats=Avg('available_seats'))

    # station with max onboard frequency
    max_onboard_station = Station.objects.order_by('onboard_frequency').first()
    # station with max offboard frequency
    max_offboard_station = Station.objects.order_by('-offboard_frequency').first()

    response_data = {
        'avg_total_duration': avg_duration['avg_duration'],
        'avg_total_passengers': avg_passengers['avg_passengers'],
        'avg_total_seats': avg_seats['avg_seats'],
        'max_onboard_station': {
            'station_name': max_onboard_station.station_name,
            'onboard_frequency': max_onboard_station.onboard_frequency
        } if max_onboard_station else None,
        'max_offboard_station': {
            'station_name': max_offboard_station.station_name,
            'offboard_frequency': max_offboard_station.offboard_frequency
        } if max_offboard_station else None
    }

    return Response(response_data)