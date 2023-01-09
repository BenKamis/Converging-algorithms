#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 7 14:37:09 2023

@author: Ben Kamis

File: fractioncalculator.py
    
Description: This is just a fun project I came up with. These are two algorithms that
start at 0 or 1 and converge to a float and return a fraction. The fraction is only
simplified if the float input shares a common factor with 10, aka 2 or 5.
"""

import matplotlib.pyplot as plt

def user_input():
    '''
    name: user_input
    This function takes a user input and either calls itself, another function,
    or two other functions based on the input.
    parameters: None
    return: None
    '''
    input_num = input("Please input a float, or input 'exit' to go back: ")
    # Returns to the prior prompt
    if input_num == "exit":
        main()
        user_input()
    # If the user inputs a float, both algorithms are applied and a graph is
    # displayed with the count times for each
    try:
        float(input_num)
        fraction_calc_method_one(input_num, True)
        fraction_calc_method_two(input_num, True)
        user_input()
    # If the user does not input a float or "exit", this function is re-run
    except ValueError:
        print("Please input a float next time.")      
        user_input()

def fraction_calc_method_one(input_num, boo):
    '''
    name: fraction_calc_method_one
    This is one method of converging a fraction to a float. The fraction is initially
    0/1. After each loop, if the decimal places are not equal to the fraction,
    one of two actions is performed: If the fraction is too small, the numerator
    is increased by 1. If the fraction is too large, the numerator is decreased
    by 1 and the denominator is increased by 1. After each loop where one of these
    actions is performed, the count increases by 1. The graph of the fraction's
    "journey" toward the float is graphed if it was user-input.
    parameters: A float to converge to and a boolean that controls whether or
    not to display the graph
    return: The number of loop iterations required to converge, an int
    '''
    # The fraction converging only concerns the digits after the decimal point.
    # This part removes the concern for the digits before the decimal
    input_num = float(input_num)
    rounded_input = round(input_num)
    # After 7 digits of decimals, the fraction is approximated to the float.
    decimals = round(input_num - rounded_input, 7)
    
    # Initializing variables
    numerator = 0
    denominator = 1
    count = 0
    test_frac = round(numerator / denominator, 7)
    # Graph is only generated for user-inputted floats
    if boo == True:
        x_axis = []
        y_axis = []
    
    while test_frac != decimals:
        # Graph is only generated for user-inputted floats
        if boo == True:
            x_axis.append(count)
            y_axis.append(test_frac + rounded_input)
        # If the fraction is too low, add to the numerator
        if test_frac < decimals:
            numerator += 1
        # If the fraction is too high, undo the last addition and add to the denominator
        elif test_frac > decimals:
            numerator -= 1
            denominator += 1
        # Re-calculate the fraction that's being tested and increase the iteration count
        test_frac = numerator / denominator
        count += 1
    # Graph is only generated for user-inputted floats
    if boo == True:
        x_axis.append(count)
        y_axis.append(test_frac + rounded_input)
        plt.plot(x_axis, y_axis, c = "b")
        plt.scatter(count, input_num, s = 50, c = "g")
        plt.text(count, input_num+0.1, "Algorithm 1", size = 15, c = "b")
        plt.xlabel("Number of steps")
        plt.ylabel("Fraction reached (in decimal form)")
        plt.title("Fraction progress toward float input")
        # The graph is not shown yet because the second method will be applied
        # and graphed onto the same plot
    # The digits before the decimal point were disregarded, they are added back here
    # and the fraction is an improper fraction if the float was not between -1 and 1
    final_numerator = denominator * rounded_input + numerator
    # Output message is only sent for user-inputted floats
    if boo == True:
        print("First algorithm calculated:", final_numerator, "/", denominator, "in:", count, "steps")
    
    return(count)

def fraction_calc_method_two(input_num, boo):
    '''
    name: fraction_calc_method_two
    This is another method of converging a fraction to a float. The fraction is
    initially 1/1. After each loop, if the decimal places are not equal to the fraction,
    one of two actions is performed: If the fraction is too small, the numerator
    is increased by 1. If the fraction is too large, the numerator is decreased
    by 1 and the denominator is increased by 1. After each loop where one of these
    actions is performed, the count increases by 1. The graph of the fraction's
    "journey" toward the float is graphed if it was user-input.
    parameters: A float to converge to and a boolean that controls whether or
    not to display the graph
    return: The number of loop iterations required to converge, an int
    '''
    # The fraction converging only concerns the digits after the decimal point.
    # This part removes the concern for the digits before the decimal
    input_num = float(input_num)
    rounded_input = round(input_num)
    # After 7 digits of decimals, the fraction is approximated to the float.
    decimals = round(input_num - rounded_input, 7)
    # A bit of an odd fix I had was when the float was negative and rounded down
    # or positive and rounded up. This fix was not necessary in the other method
    # because the numerator can be 0 or negative, but in this method the denominator
    # cannot become 0 or negative. Thus, if the float is between 0.5 and 1 or
    # -0.5 and 0, it is rounded up, and this method will be calculating the fraction
    # the float is away from the number rounded up, not down. It must be subtracted
    # from the float, instead of being added to it like in method one.
    rounded_up = False
    if decimals < 0:
        decimals = abs(decimals)
        rounded_up = True
        
    # Initializing Variables
    numerator = 1
    denominator = 1
    test_frac = round(numerator / denominator, 7)
    count = 0
    # Graph is only generated for user-inputted floats
    if boo == True:
        x_axis = []
        y_axis = []
    while test_frac != decimals:
        # Graph is only generated for user-inputted floats
        if boo == True:
            x_axis.append(count)
            # If the input was rounded up, the float must be subtracted, as
            # explained a few comments up
            if rounded_up == True:
                y_axis.append(-test_frac + rounded_input)
            else:
                y_axis.append(test_frac + rounded_input)
        # If the fraction is too high, add to the denominator
        if test_frac > decimals:
            denominator += 1
        # If the fraction is too low, add to the numerator and undo the last step
        # ONLY if the denominator is not 1. If undone, the denominator would be 0,
        # leading to an arithmetic error
        elif test_frac < decimals:
            numerator += 1
            if denominator != 1:
                denominator -= 1         
        # In the case that the fraction should approach 0, it will get infinitely
        # close (as the denominator tends to infinity) but never exactly arrive
        # (without rounding) and drive up the computation time. This special case
        # is solved in this if statement, and this check will count as 1 "count".
        if decimals == 0:
            numerator = 0
            denominator = 1
        # Re-calculate the fraction that's being tested and increase the iteration count
        test_frac = numerator / denominator
        count += 1
    # Graph is only generated for user-inputted floats
    if boo == True:
        x_axis.append(count)
        # If the input was rounded up, the float must be subtracted, as
        # explained a few comments up
        if rounded_up == True:
            y_axis.append(-test_frac + rounded_input)
        else:
            y_axis.append(test_frac + rounded_input)
        plt.plot(x_axis, y_axis, c = "r")
        plt.scatter(count, input_num, s = 50, c = "g")
        plt.text(count, input_num-0.1, "Algorithm 2", size = 15, c = "r")
        plt.xlabel("Number of steps")
        plt.ylabel("Fraction reached (in decimal form)")
        plt.title("Fraction progress toward float input")
        # The graph is shown now that both functions have been applied to the float
        plt.show()
    
    # If the input was rounded up, the numerator must be subtracted, as
    # explained a few comments up
    if rounded_up == True:
        final_numerator = denominator * rounded_input - numerator
    else:
        final_numerator = denominator * rounded_input + numerator
    
    # Output message is only sent for user-inputted floats
    if boo == True:
        print("Second algorithm calculated:", final_numerator, "/", denominator, "in:", count, "steps")
    
    return(count)

def graph_generator():
    '''
    name: graph_generator
    Using both converging algorithms on values over an interval of 1, two graphs
    are created. The first graph shows the number of loop iterations required fpr
    each algorithm to converge for each value tested. The second graph shows
    which algorithm converged faster for each point and how many loop iterations
    were required for it to converge. Both graphs repeat with a period of 1.
    parameters: None
    return: None
    '''
    # Initializing variables
    input_num = 0
    end_num = input_num + 1
    intervals = 0.001
    count_1_list = []
    count_2_list = []
    num_list = []
    compare_list = []
    while input_num <= end_num:
        # Both algorithms are applied to each float in the interval. The number of
        # loop iterations to reach the number is added to a list fo each algorithm
        count_1 = fraction_calc_method_one(input_num, False)
        count_2 = fraction_calc_method_two(input_num, False)
        count_1_list.append(count_1)
        count_2_list.append(count_2)
        num_list.append(input_num)
        
        # For each float tested, the algorithm with a lower loop iteration number
        # and the number of iterations is saved in a new list with other attributes
        # to be plotted
        if count_1 < count_2:
            lower_count = count_1
            color = "b"
            size = 5
        elif count_1 > count_2:
            lower_count = count_2
            color = "r"
            size = 5
        elif count_1 == count_2:
            lower_count = count_1
            color = "g"
            size = 40
        # Each float tested gets a compare_list with attributes to be plotted
        # one by one
        compare_list.append([round(lower_count, 7), color, size, round(input_num, 7)])
        input_num += intervals
    
    # First graph
    plt.xlabel("Float tested")
    plt.ylabel("Number of fraction iteration steps")
    plt.title("Fraction progress toward float input")
    plt.scatter(num_list, count_1_list, s = 5, c = "b")    
    plt.scatter(num_list, count_2_list, s = 5, c = "r")
    plt.show()
    # Second graph
    plt.xlabel("Float tested")
    plt.ylabel("Number of fraction iteration steps")
    plt.title("Comparing two fraction finding algorithms")
    plt.text(0, max(count_2_list)*0.95, "Algorithm 1", size = 15, c = "b")
    plt.text(0, max(count_2_list)*0.85, "Algorithm 2", size = 15, c = "r")
    # Each point in the second graph being plotted one by one
    for i in compare_list:
        plt.scatter(i[3], i[0], c = i[1], s = i[2])
    plt.show()
    main()
    
def first_user_input():
    '''
    name: first_user_input
    The user can choose to input their own float and visualization as the algorithms
    fractions approaching that float, or view different visualizations of the
    number of loop iterations required by each algorithm to reach many floats
    parameters: None
    return: choice, a string
    '''
    choice = input("Press 1 to input a float. Press anything else to see graphs.")
    return(choice)

def main():
    
    choice = first_user_input()
    # Applies both converging algorithms to a user-inputted float
    if choice == "1":
        user_input()
    # Displays graphs for floats over a range
    else:
        graph_generator()
        
if __name__ == "__main__":
    main()