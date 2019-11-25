from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import Rack, Pdu 
from items.serializers import RackSerializer, PduSerializer

error_messages = {
    'RETRIEVE_ERROR': 'Rack object could not found.',
    'UPDATE_ERROR': 'Failed to update rack object'
}

@api_view(['GET'])
def api_root(request, format=None):
    return Response([
        reverse('items:racks-list', request=request, format=format),
        reverse('items:pdu-list', request=request, format=format),
    ])

class RackView(generics.ListCreateAPIView):
    queryset = Rack.objects.all()
    serializer_class = RackSerializer
    filter_backends = [SearchFilter]
    search_fields = ['id', 'height', 'location', 'color']


# @api_view(['GET', 'POST'])
# def rack_list(request):
#     """List all rack objects or create a new rack object"""
#     if request.method == 'GET':
#         racks = Rack.objects.all()
#         serializer = RackSerializer(racks, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = RackSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(
#             serializer.errors, 
#             status=status.HTTP_400_BAD_REQUEST, 
#             data={'message': error_messages.get('CREATE_ERROR')}
#         )

@api_view(['GET', 'PUT'])
def rack_detail(request, pk):
    """Retrieve or update a rack object"""
    try:
        rack = Rack.objects.get(pk=pk)
    except Rack.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': error_messages.get('RETRIEVE_ERROR')})

    if request.method == 'PUT':
        serializer = RackSerializer(rack, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, 
            status=status.HTTP_400_BAD_REQUEST, 
            data={'message': error_messages.get('UPDATE_ERROR')}
        )    
    elif request.method == 'GET':
        serializer = RackSerializer(rack)
        return Response(serializer.data)


class PduListCreateSearchView(generics.ListCreateAPIView):
    queryset = Pdu.objects.all()
    serializer_class = PduSerializer
    filter_backends = [SearchFilter]
    search_fields = ['brand', 'capacity', 'num_outlets']


class PduRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Pdu.objects.all()
    serializer_class = PduSerializer
