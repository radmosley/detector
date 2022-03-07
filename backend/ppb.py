import os
import json
import sys
import django 
from api.senator.models import Senator

django.setup()

sys.path.append('/Users/ronniemosley/SynologyDrive/projects/code/detector/backend/api/senator')

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
def run():
    with open('test_data.json', 'r') as f:
        print("Reading json")
        data = json.load(f)
        #print(data['results'][0]['members'])
        for x in data['results'][0]['members']:
            #load model 
            senator = Senator({
                'senate_id': data['id'],
                'first_name': data['first_name'],
                'last_name': data['last_name'],
                })
            senator.save()
            print("Senator Complete")
        return
if __name__ == "__main__":
    run()
