from django.core.management.base import BaseCommand, CommandError
from polls.models import Question as Poll

class Command(BaseCommand):
    help = 'Import JSON to project'
    
    def create():
        pass


# senators = loadjsonfile
# for senator in senators:
# for item in senator:
# if item.key == model.key:
# senator_update = []
# senator_update.append(item.value)
# loadtojson(senator_update)
