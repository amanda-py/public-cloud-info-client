import lib.susepubliccloudinfoclient.infoserverrequests as ifsrequest
import json

#creating my variables:
choosed_date = 20230612
ordering_dates = []

#testing the output with amazon images 
result = ifsrequest.get_image_data(
        'amazon', None, 'json', 'us-east-1'
    )

#getting the all data
data = json.loads(result)

#getting the data information (AAAA-MM-DD)
for n in range(len(data['images'])):
    day = int(data['images'][n]["publishedon"])
    
    if day > choosed_date:
        ordering_dates.append(data['images'][n])

for image in ordering_dates:
    if 'publishedon' not in image:
        print("00000")
    print(f"{image['publishedon']}...{image['name']}...")