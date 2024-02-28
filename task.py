import lib.susepubliccloudinfoclient.infoserverrequests as ifsrequest
import json

#creating my variable:
choosed_date = 20230612

#defining a way to get images from all providers:
def get_all_images_results(date):
    
    #defining a list with all providers:
    providers = ["microsoft",
                "amazon"
                "oracle"
                "alibaba"
                "google"]

    data = []
    for provider in providers:
        new_images = ifsrequest.get_image_data(provider, None, 'json', command_arg_filter=f"publishedon>{date}")
        new_images = json.loads(new_images)
        # Adding the all the information in data
        data += new_images["images"]

    return data



#filtering the output on my way :D
def filtering_results(date):
    images = get_all_images_results(date)

    for image in images:
        #setting the date
        date = str(images["publishedon"])
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        format_date = f"{year}/{month}/{day}"

        #setting the url
        url = "[URL not provided]"
        if "changeinfo" in images:
            url = images["changeinfo"]
        
        print(f'{format_date}: {images["name"]}-------------------{url}')
        
        
filtering_results(choosed_date)