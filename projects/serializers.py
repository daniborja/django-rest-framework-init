from rest_framework import serializers

# ### Serializers based on Existing Models
from .models import Project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        # fields q podran ser consultados
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        # fields q son solo de lectura para evitar su manipulacion
        read_only_fields = ('created_at', )


