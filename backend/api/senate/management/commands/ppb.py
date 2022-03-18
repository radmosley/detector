from django.core.management.base import BaseCommand
from ...models import Senator
import json

class Command(BaseCommand):
    help = 'Displays current time'
    def add_arguments(self, parser):
        parser.add_argument('senate_file', type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs['senate_file'], 'r') as f:
            print("Reading json")
            data = json.load(f)
        for member in data['results'][0]['members']:
            print("loading member")
            # new_member = member['first_name'] + " " + member['last_name']
        # # load model
            try:
                obj = Senator.objects.get(senate_id=member['id'])
            except Senator.DoesNotExist:
                senator = Senator.objects.get_or_create(
                    senate_id = member['id'],
                    title = member['title'],
                    party = member['party'],
                    first_name = member['first_name'],
                    last_name = member['last_name'],
                )
                print("Complete")