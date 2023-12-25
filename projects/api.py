from .models import Project


from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer



# ### Define q consultas se van a poder hacer
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny] # todos pueden hacer esta consulta
    serializer_class = ProjectSerializer  # serializer q atendera este viewset


