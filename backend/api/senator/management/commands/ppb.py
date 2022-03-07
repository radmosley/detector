from django.core.management.base import BaseCommand
from django.utils import timezone
from ...models import Senator
import json

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        #load json
        with open('test_data.json', 'r') as f:
            data = json.load(f)
        for x in data['results'][0]['members']:
            new_member = x['first_name'] + " " + x['last_name']
        # load model
            senator = Senator(
                senate_id = x['id'],
                title = x['title'],
                party = x['party'],
                first_name = x['first_name'],
                last_name = x['last_name'],
            )
            senator.save()
            print(new_member + " complete")
            # print(x['id'])
        # time = timezone.now().strftime('%X')
        # Console log
        # self.stdout.write("It's now %s" % time)