from rest_framework import serializers
from .models import User, Journal, Entry

class JournalSerializer(serializers.HyperlinkedModelSerializer):
    # entry = serializers.HyperlinkedRelatedField(
    #     view_name = 'journal_detail',
    #     many = True,
    #     read_only = True
    # )
    class Meta:
        model = Journal
        fields = ('id', 'journal_name', 'journal_date_start', 'journal_date_end', 'journal_ongoing')

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    journal = serializers.HyperlinkedRelatedField(
        view_name = 'entry_detail',
        read_only = True
    )
    class Meta:
        model = Entry
        fields = ('id', 'name', 'writeup', 'photo_album', 'journal')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    journal = serializers.HyperlinkedRelatedField(
        view_name = 'journal_detail',
        read_only = True
    )
    class Meta:
        model = User
        fields = ('__all__')