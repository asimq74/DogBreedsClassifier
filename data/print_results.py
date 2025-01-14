#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
from tabulate import tabulate


def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification in tabular format and optionally prints
    incorrectly classified dogs and dog breeds.
    """
    print(f"\n*** Results Summary for CNN Model Architecture: {model.upper()} ***\n")

    stats_table = [
        ["# Total Images", results_stats_dic["n_images"]],
        ["# Dog Images", results_stats_dic["n_dogs_img"]],
        ["# Not-a-Dog Images", results_stats_dic["n_notdogs_img"]]
    ]

    # Print the overall statistics in the specified format
    print("Overall Statistics:")
    print(tabulate(stats_table, headers=["Metric", "Value"], tablefmt="grid"))

    # Create Model Percentages Table with Formatted Percentages
    model_percentages_table = [
        ["CNN Model Architecture", "% Not-a-dog Correct", "% Dogs Correct", "% Breeds Correct", "% Match Labels"],
        [model,
         f"{results_stats_dic['pct_correct_notdogs']:.1f}%",
         f"{results_stats_dic['pct_correct_dogs']:.1f}%",
         f"{results_stats_dic['pct_correct_breed']:.1f}%",
         f"{results_stats_dic['pct_match']:.1f}%"]
    ]

    # Print the table
    print("Model-Specific Percentages:")
    print(tabulate(model_percentages_table, tablefmt="grid"))

    # Prepare and print the overall statistics in a table
    stats_table = [[key, f"{value:.2f}%" if key.startswith('pct') else value]
                   for key, value in results_stats_dic.items()]

    print("Overall Statistics:")
    print(tabulate(stats_table, headers=["Metric", "Value"], tablefmt="grid"))

    # Print incorrectly classified dogs in tabular format if requested
    if print_incorrect_dogs:
        print("\nIncorrectly Classified Dogs:")
        dog_rows = [
            [filename, data[0], data[1]]
            for filename, data in results_dic.items() if data[3] != data[4]
        ]
        if dog_rows:
            print(tabulate(dog_rows, headers=["Filename", "True Label", "Classifier Label"], tablefmt="grid"))
        else:
            print("No incorrectly classified dog images.")

    # Print incorrectly classified breeds in tabular format if requested
    if print_incorrect_breed:
        print("\nIncorrectly Classified Dog Breeds:")
        breed_rows = [
            [filename, data[0], data[1]]
            for filename, data in results_dic.items() if data[3] == 1 and data[4] == 1 and data[2] == 0
        ]
        if breed_rows:
            print(tabulate(breed_rows, headers=["Filename", "True Label", "Classifier Label"], tablefmt="grid"))
        else:
            print("No incorrectly classified dog breeds.")

    print("\n*** End of Results ***")
