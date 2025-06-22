from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet): # ViewSet for handling patient records apis
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


'''
#POST
#Endpoint: http://127.0.0.1:8000/api/patients/
#Body:{
  "name": "Shreyas",
  "age": 30,
  "disease": "Flu"
}

#Respond:
{
  "id": 2,
  "name": "Shreyas",
  "age": 30,
  "disease": "Flu",
  "created_at": "2025-06-21T12:47:16.657422Z",
  "user": 1
}

#GET
#Endpoint: http://127.0.0.1:8000/api/patients/
# Respond:
# [
  {
    "id": 2,
    "name": "Shreyas",
    "age": 30,
    "disease": "Flu",
    "created_at": "2025-06-21T12:47:16.657422Z",
    "user": 1
  }
]

'''