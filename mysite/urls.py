"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from booksapi.views import BookViewSet, AdventureFictionViewSet, HistoricalFictionViewSet, BildungsromanViewSet, \
                           FictionViewSet, DramaViewSet, SatireViewSet, SouthernGothicViewSet, RomanceViewSet, \
                           MagicalRealismViewSet, PhilosophicalFictionViewSet, ThreesViewSet, FoursViewSet
from django.conf.urls.static import static
from django.conf import settings


router = routers.SimpleRouter()
router.register('books', BookViewSet)
router.register('adventurefiction', AdventureFictionViewSet)
router.register('historicalfiction', HistoricalFictionViewSet)
router.register('bildungsroman', BildungsromanViewSet)
router.register('fiction', FictionViewSet)
router.register('drama', DramaViewSet)
router.register('satire', SatireViewSet)
router.register('southerngothic', SouthernGothicViewSet)
router.register('romance', RomanceViewSet)
router.register('magicalrealism', MagicalRealismViewSet)
router.register('philosophicalfiction', PhilosophicalFictionViewSet)
router.register('threes', ThreesViewSet)
router.register('fours', FoursViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
