import lib.susepubliccloudinfoclient.infoserverrequests as ifsrequest
import json

# testing the output with amazon images 
result = ifsrequest.get_image_data(
        'amazon', None, 'json', 'us-east-1'
    )

data = json.loads(result)

print(result, data['images'][0]["publishedon"])