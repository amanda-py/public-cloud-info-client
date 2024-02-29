#!/usr/bin/env python3

import task as task
import argparse

date_image_filter = argparse.ArgumentParser(description='Filter images from a date specified by a user')

date_image_filter.add_argument('date', type=int, help='Specify a data you want to see all images after it. The data format is: AAAAMMDD')

args = date_image_filter.parse_args()

x = task.filtering_results(args.date)

if __name__=='__main__':
    print(x)