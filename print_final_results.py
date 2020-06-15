#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#                                                                             
# PROGRAMMER: Andrew Renn                                                    
# DATE CREATED: 10/06/2020                                                 
# PURPOSE:  This function simply prints the results of all of the
#           classifier functions in one neat table
#
##

def print_final_results():
    filenames = ["resnet_pet-images.txt", "resnet_uploaded-images.txt",
                 "vgg_pet-images.txt", "vgg_uploaded-images.txt",
                 "alexnet_pet-images.txt", "alexnet_uploaded-images.txt"]


    results_dic = {"resnet_pet-images": [" "]*4,
                    "resnet_uploaded-images": [" "]*4,
                    "vgg_pet-images": [" "]*4,
                    "vgg_uploaded-images": [" "]*4,
                    "alexnet_pet-images": [" "]*4,
                    "alexnet_uploaded-images": [" "]*4}

    for file in filenames:
        with open(file) as f:
            modelname = file.split(".")[0].strip()
            for line in f:
                if "percentage" in line:
                    percentage = line.split(": ")[1].strip()
                    if "correct matches" in line:
                        results_dic[modelname][0] = percentage
                    elif "dog breeds" in line:
                        results_dic[modelname][1] = percentage
                    elif "NON-dogs" in line:
                        results_dic[modelname][2] = percentage
                    elif "dogs" in line:
                        results_dic[modelname][3] = percentage


    print("---------------------------------------------------------------------------------------------------------")
    print("| final results table:                                                                                  |")
    print("---------------------------------------------------------------------------------------------------------")
    print("|         Model name         | % Not-A-Dog Correct | % Dogs Correct | % Breeds Correct | % Match Labels |")
    for model, data in results_dic.items():
        print("|", model + " "*(26-len(model)), "|", " "*(19-len(data[2]))+ data[2], "|",
                " "*(14-len(data[3]))+ data[3], "|",
                " "*(16-len(data[1]))+ data[1], "|",
                " "*(14-len(data[0]))+ data[0], "|")
    print("---------------------------------------------------------------------------------------------------------")

if __name__ == "__main__":
   print_final_results()