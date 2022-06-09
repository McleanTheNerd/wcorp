from django.urls import path, include
# from django.contrib.auth.models import User
from api.models import WCORP
from api.models.proposals import Project,Proposal
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WCORP
        fields = ['url', 'username', 'email', 'is_staff']

class ProposalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proposal
        fields = ['url', 'id', 'topic','proposal_text','date_posted']

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'id', 'title','github_link','date_published']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = WCORP.objects.all()
    serializer_class = UserSerializer

class ProposalViewSet(viewsets.ModelViewSet):
    queryset = Proposal.objects.all()
    serializer_class = ProposalSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'proposals', ProposalViewSet)
router.register(r'projects', ProjectViewSet)