from rest_framework import routers

from .api import ProjectViewSet


# ### Routes with REST Framework
router = routers.DefaultRouter()

# ## ruta, ViewSet, ruouteName
# Esta ruta ya crea todos los Verbos HTTP: POST/PUT/DEL con / al final: {{url}}/api/projects/5/
# Verbos NO idempotentes con   /   al final de la url
router.register('api/projects', ProjectViewSet, 'projects')


urlpatterns = router.urls
