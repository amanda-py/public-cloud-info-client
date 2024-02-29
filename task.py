import lib.susepubliccloudinfoclient.infoserverrequests as ifsrequest
import json

#creatinf my variable
choosed_date = 20230612

#defining a way to get images from all providers
def get_all_image_results(date):
    # List all the used providers
    providers = [
        "microsoft",
        "amazon",
        "oracle",
        "alibaba",
        "google"
    ]

    results = []
    for provider in providers:
        # Get all results from a specific provider(microsoft, amazon, ...)
        new_images = ifsrequest.get_image_data(provider, None, 'json', command_arg_filter=f"publishedon>{date}")
        new_images = json.loads(new_images)

        # Add result in "results"
        results += new_images["images"]

    return results

#filtering the output on my way
def filtering_results(date):
    images = get_all_image_results(date)

    for image in images:
        date = str(image["publishedon"])
        year = date[:4]
        month = date[4:6]
        day = date[6:]
        fdate = f"{year}/{month}/{day}"

        url = "[URI Not Provided]"
        if "changeinfo" in image:
            url = image["changeinfo"]

        print(f'{fdate}: {image["name"]} ------------ {url}')

filtering_results(choosed_date)