from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Senator
import json

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        with open('test_data.json', 'r') as f:
            print("Reading json")
            data = json.load(f)
        for x in data['results'][0]['members']:
            print("loading member")
            new_member = x['first_name'] + " " + x['last_name']
        # # load model
            senator = Senator.objects.get_or_create(
                senate_id = x['id'],
                title = x['title'],
                party = x['party'],
                first_name = x['first_name'],
                last_name = x['last_name'],
            )
            print("Complete")