'''from django.urls import include, path
from rest_framework import routers
from tutorial.quickstart import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]'''

'''from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('polls/', include('polls.urls')),
    path('', include('myapi.urls')),
    path('admin/', admin.site.urls),
]
'''

'''from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('polls',include('polls.urls')),
    path('admin/', admin.site.urls),
]'''

from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    #path('api/',include('api.urls')),
    path('products/',include('products.urls')),
    path('categories/',include('products.urls')),
    path('sellers/',include('products.urls')),
    path('admin/', admin.site.urls),
]