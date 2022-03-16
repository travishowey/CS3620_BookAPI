from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import BookData
from django.db.models import Q


# Create your views here.


class BookViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.all()
    serializer_class = BookSerializer


class AdventureFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Adventure Fiction')
    serializer_class = BookSerializer


class HistoricalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Historical Fiction')
    serializer_class = BookSerializer


class BildungsromanViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Bildungsroman')
    serializer_class = BookSerializer


class FictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Fiction')
    serializer_class = BookSerializer


class DramaViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Drama')
    serializer_class = BookSerializer


class SatireViewSet(viewsets.ModelViewSet):
        queryset = BookData.objects.filter(category='Satire')
        serializer_class = BookSerializer


class SouthernGothicViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Southern Gothic')
    serializer_class = BookSerializer


class RomanceViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Romance')
    serializer_class = BookSerializer


class MagicalRealismViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Magical Realism')
    serializer_class = BookSerializer


class PhilosophicalFictionViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(category='Philosophical Fiction')
    serializer_class = BookSerializer


class ThreesViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(rating='3.0') | Q(rating='3.1') | Q(rating='3.2') | Q(rating='3.3')\
                                        | Q(rating='3.4') | Q(rating='3.5') | Q(rating='3.6') | Q(rating='3.7')\
                                        | Q(rating='3.8') | Q(rating='3.9'))
    serializer_class = BookSerializer


class FoursViewSet(viewsets.ModelViewSet):
    queryset = BookData.objects.filter(Q(rating='4.0') | Q(rating='4.1') | Q(rating='4.2') | Q(rating='4.3')\
                                        | Q(rating='4.4') | Q(rating='4.5') | Q(rating='4.6') | Q(rating='4.7')\
                                        | Q(rating='4.8') | Q(rating='4.9'))
    serializer_class = BookSerializer