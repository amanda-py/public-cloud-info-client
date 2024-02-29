#!/usr/bin/env python3

import task as task
import argparse

#creating the object with a description
date_image_filter = argparse.ArgumentParser(description='Filter images from a date specified by a user')

#Adding the argument using only the paramether date
date_image_filter.add_argument('date', type=int, help='Specify a data you want to see all images after it. The data format is: AAAAMMDD')


#setting the filter fuction
args = date_image_filter.parse_args()

# saving all data in this variable imagens
imagens = task.filtering_results(args.date)

#printing in the CLI
if __name__=='__main__':
    print(imagens)