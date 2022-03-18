import os
import json
import sys
import django 
from api.senate.models import Senator

django.setup()

sys.path.append('/Users/ronniemosley/SynologyDrive/projects/code/detector/backend/api/senate')

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
def run():
    with open('test_data.json', 'r') as f:
        print("Reading json")
        data = json.load(f)
    for member in data['results'][0]['members']:
        print("loading member")
        # new_member = member['first_name'] + " " + member['last_name']
    # # load model
        try:
            obj = Senator.objects.get(senate_id=member['id'])
        except Senator.DoesNotEmemberist:
            senator = Senator.objects.get_or_create(
                senate_id = member['id'],
                title = member['title'],
                party = member['party'],
                first_name = member['first_name'],
                last_name = member['last_name'],
            )
            print("Complete")
        return
if __name__ == "__main__":
    run()
