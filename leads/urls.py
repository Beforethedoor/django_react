from rest_framework import routers
from .api import LeadVeiwSet

routers = routers.DefaultRouter()
routers.register('api/leads', LeadVeiwSet, 'leads')

urlpatterns = routers.urls
