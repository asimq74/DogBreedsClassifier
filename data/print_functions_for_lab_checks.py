#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/print_functions_for_lab_checks.py
#                                                                             
# PROGRAMMER: Jennifer S.                                                    
# DATE CREATED: 05/14/2018                                  
# REVISED DATE:             <=(Date Revised - if any)                         
# PURPOSE:  This set of functions can be used to check your code after programming 
#           each function. The top section of each part of the lab contains
#           the section labeled 'Checking your code'. When directed within this
#           section of the lab one can use these functions to more easily check 
#           your code. See the docstrings below each function for details on how
#           to use the function within your code.
#
##

# Functions below defined to help with "Checking your code", specifically
# running these functions with the appropriate input arguments within the
# main() funtion will print out what's needed for "Checking your code"
#
def check_command_line_arguments(in_arg):
    """
    For Lab: Classifying Images - 7. Command Line Arguments
    Prints each of the command line arguments passed in as parameter in_arg, 
    assumes you defined all three command line arguments as outlined in 
    '7. Command Line Arguments'
    Parameters:
     in_arg -data structure that stores the command line arguments object
    Returns:
     Nothing - just prints to console  
    """
    if in_arg is None:
        print("* Doesn't Check the Command Line Arguments because 'get_input_args' hasn't been defined.")
    else:
        # prints command line agrs
        print("Command Line Arguments:\n     dir =", in_arg.dir, 
              "\n    arch =", in_arg.arch, "\n dogfile =", in_arg.dogfile)

def check_creating_pet_image_labels(results_dic):
    """    For Lab: Classifying Images - 9/10. Creating Pet Image Labels
    Prints first 10 key-value pairs and makes sure there are 40 key-value 
    pairs in your results_dic dictionary. Assumes you defined the results_dic
    dictionary as was outlined in 
    '9/10. Creating Pet Image Labels'
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
    Returns:
     Nothing - just prints to console  
    """
    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'get_pet_labels' hasn't been defined.")
    else:
        # Determine the number of entries to print (up to 10)
        stop_point = min(len(results_dic), 10)

        print("\nPet Image Label Dictionary has", len(results_dic), "key-value pairs.")
        print(f"Below are the first {stop_point} key-value pairs displayed in a table format:\n")

        # Print table header
        print("{:<5} {:<30} {:<30}".format("No.", "Filename (Key)", "Pet Image Label"))
        print("-" * 70)

        # Counter to track how many labels have been printed
        n = 0

        # Iterate through the dictionary and print the first 10 labels
        for key in results_dic:
            if n < stop_point:
                print("{:<5} {:<30} {:<30}".format(n + 1, key, results_dic[key][0]))
                n += 1
            else:
                break


def check_classifying_images(results_dic):
    """    For Lab: Classifying Images - 11/12. Classifying Images
    Prints Pet Image Label and Classifier Label for ALL Matches followed by ALL 
    NOT matches. Next prints out the total number of images followed by how 
    many were matches and how many were not-matches to check all 40 images are
    processed. Assumes you defined the results_dic dictionary as was 
    outlined in '11/12. Classifying Images'
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
    Returns:
     Nothing - just prints to console  

    """
    from tabulate import tabulate

    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 2:
        print("* Doesn't Check the Results Dictionary because 'classify_images' hasn't been defined.")
    else:
        # Sets counters for matches & NOT-matches
        n_match = 0
        n_notmatch = 0

        # Prepare data for Matches table
        match_table = [["Image", "Real Label", "Classifier Label"]]
        for key in results_dic:
            # Add Matches to the table if Index 2 == 1
            if results_dic[key][2] == 1:
                n_match += 1
                match_table.append([key, results_dic[key][0], results_dic[key][1]])

        # Prepare data for NOT Matches table
        notmatch_table = [["Image", "Real Label", "Classifier Label"]]
        for key in results_dic:
            # Add NOT Matches to the table if Index 2 == 0
            if results_dic[key][2] == 0:
                n_notmatch += 1
                notmatch_table.append([key, results_dic[key][0], results_dic[key][1]])

        # Print Matches table
        print("\nMATCHES:")
        print(tabulate(match_table, headers="firstrow", tablefmt="grid"))

        # Print NOT Matches table
        print("\nNOT A MATCH:")
        print(tabulate(notmatch_table, headers="firstrow", tablefmt="grid"))

        # Print Total Images Summary
        print("\nSummary:")
        print(f"Total Images: {n_match + n_notmatch}, Matches: {n_match}, NOT Matches: {n_notmatch}")


def check_classifying_labels_as_dogs(results_dic):
    """    For Lab: Classifying Images - 13. Classifying Labels as Dogs
    Prints Pet Image Label, Classifier Label, whether Pet Label is-a-dog(1=Yes,
    0=No), and whether Classifier Label is-a-dog(1=Yes, 0=No) for ALL Matches 
    followed by ALL NOT matches. Next prints out the total number of images 
    followed by how many were matches and how many were not-matches to check 
    all 40 images are processed. Assumes you defined the results_dic dictionary
    as was outlined in '13. Classifying Labels as Dogs'
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
    Returns:
     Nothing - just prints to console  

    """
    from tabulate import tabulate

    if results_dic is None:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    elif len(results_dic[next(iter(results_dic))]) < 4:
        print("* Doesn't Check the Results Dictionary because 'adjust_results4_isadog' hasn't been defined.")
    else:
        # Sets counters for matches & NOT-matches
        n_match = 0
        n_notmatch = 0

        # Prepare data for Matches table
        match_table = [["Image", "Real Label", "Classifier Label", "PetLabelDog", "ClassLabelDog"]]
        for key in results_dic:
            # Add Matches to the table if Index 2 == 1
            if results_dic[key][2] == 1:
                n_match += 1
                match_table.append([
                    key,
                    results_dic[key][0],
                    results_dic[key][1],
                    results_dic[key][3],
                    results_dic[key][4]
                ])

        # Prepare data for NOT Matches table
        notmatch_table = [["Image", "Real Label", "Classifier Label", "PetLabelDog", "ClassLabelDog"]]
        for key in results_dic:
            # Add NOT Matches to the table if Index 2 == 0
            if results_dic[key][2] == 0:
                n_notmatch += 1
                notmatch_table.append([
                    key,
                    results_dic[key][0],
                    results_dic[key][1],
                    results_dic[key][3],
                    results_dic[key][4]
                ])

        # Print Matches table
        print("\nMATCHES:")
        print(tabulate(match_table, headers="firstrow", tablefmt="grid"))

        # Print NOT Matches table
        print("\nNOT A MATCH:")
        print(tabulate(notmatch_table, headers="firstrow", tablefmt="grid"))

        # Print Total Images Summary
        print("\nSummary:")
        print(f"Total Images: {n_match + n_notmatch}, Matches: {n_match}, NOT Matches: {n_notmatch}")


def check_calculating_results(results_dic, results_stats_dic):
    """    For Lab: Classifying Images - 14. Calculating Results
    Prints First statistics from the results stats dictionary (that was created
    by the calculates_results_stats() function), then prints the same statistics
    that were calculated in this function using the results dictionary.
    Assumes you defined the results_stats dictionary and the statistics 
    as was outlined in '14. Calculating Results '
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)   where 1 = match between pet image and 
                    classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     results_stats_dic - Dictionary that contains the results statistics (either
                     a percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
    Returns:
     Nothing - just prints to console  

    """
    from tabulate import tabulate

    if results_stats_dic is None:
        print("* Doesn't Check the Results Dictionary because 'calculates_results_stats' hasn't been defined.")
    else:
        # Code for checking results_stats_dic -
        # Checks calculations of counts & percentages BY using results_dic
        # to re-calculate the values and then compare to the values
        # in results_stats_dic

        # Initialize counters to zero and number of images total
        n_images = len(results_dic)
        n_pet_dog = 0
        n_class_cdog = 0
        n_class_cnotd = 0
        n_match_breed = 0

        # Interates through results_dic dictionary to recompute the statistics
        # outside of the calculates_results_stats() function
        for key in results_dic:
            # match (if dog then breed match)
            if results_dic[key][2] == 1:
                # isa dog (pet label) & breed match
                if results_dic[key][3] == 1:
                    n_pet_dog += 1
                    # isa dog (classifier label) & breed match
                    if results_dic[key][4] == 1:
                        n_class_cdog += 1
                        n_match_breed += 1
                # NOT dog (pet_label)
                else:
                    # NOT dog (classifier label)
                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1
            # NOT - match (not a breed match if a dog)
            else:
                # NOT - match
                # isa dog (pet label)
                if results_dic[key][3] == 1:
                    n_pet_dog += 1
                    # isa dog (classifier label)
                    if results_dic[key][4] == 1:
                        n_class_cdog += 1
                # NOT dog (pet_label)
                else:
                    # NOT dog (classifier label)
                    if results_dic[key][4] == 0:
                        n_class_cnotd += 1

        # calculates statistics based upon counters from above
        n_pet_notd = n_images - n_pet_dog
        pct_corr_dog = (n_class_cdog / n_pet_dog) * 100
        pct_corr_notdog = (n_class_cnotd / n_pet_notd) * 100
        pct_corr_breed = (n_match_breed / n_pet_dog) * 100

        # Create data tables
        stats_from_function = [
            ["N Images", results_stats_dic['n_images'], n_images],
            ["N Dog Images", results_stats_dic['n_dogs_img'], n_pet_dog],
            ["N NotDog Images", results_stats_dic['n_notdogs_img'], n_pet_notd],
            ["Pct Corr dog", f"{results_stats_dic['pct_correct_dogs']:.1f}", f"{pct_corr_dog:.1f}"],
            ["Pct Corr NOTdog", f"{results_stats_dic['pct_correct_notdogs']:.1f}", f"{pct_corr_notdog:.1f}"],
            ["Pct Corr Breed", f"{results_stats_dic['pct_correct_breed']:.1f}", f"{pct_corr_breed:.1f}"]
        ]

        # Print the tables
        print("\n ** Statistics from calculates_results_stats() function:")
        print(
            tabulate(stats_from_function, headers=["Metric", "Function Value", "Recalculated Value"], tablefmt="grid"))

