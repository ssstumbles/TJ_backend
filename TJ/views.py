from rest_framework import generics
from .serializers import JournalSerializer, EntrySerializer, UserSerializer
from .models import User, Entry, Journal

class JournalList(generics.ListCreateAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class JournalDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Journal.objects.all()
    serializer_class = JournalSerializer

class EntryList(generics.ListCreateAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        journal_id = self.request.query_params.get('journal', None)
        if journal_id:
            queryset = queryset.filter(journal_id=journal_id)
        return queryset

class EntryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer