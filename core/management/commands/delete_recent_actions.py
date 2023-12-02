from django.core.management.base import BaseCommand
from django.contrib.admin.models import LogEntry

class Command(BaseCommand):
    help = 'Delete recent actions'

    def handle(self, *args, **kwargs):
        LogEntry.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted recent actions.'))

