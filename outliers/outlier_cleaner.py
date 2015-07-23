#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    cleaned_data = []
    cleaned_data = [(ages[i][0], net_worths[i][0], 0) for i in range(len(predictions))]
    #print 'cleaned_data:', cleaned_data

    ### your code goes here
    #print 'predictions:', predictions
    #print 'ages', ages
    #print 'net_worths', net_worths
    cleaned_data_list = list(cleaned_data)
    print cleaned_data_list
    residual_errors = []

    # --- loop over the data and calculate the residual error ---
    for i in range(len(predictions)):
        cleaned_data_list[i][2] = abs( net_worths[i][0] - predictions[i][0] )
        residual_errors[i] = abs( net_worths[i][0] - predictions[i][0] )

    #print 'residual_errors:', residual_errors

    # --- sort residual error and remove the worst 10% ---
    sorted_residual_errors = sorted(residual_errors)
    #print 'sorted_residual_errors:', sorted_residual_errors
    cleaned_errors = sorted_residual_errors[ 0: int(0.9 * len(sorted_residual_errors)) ]
    #print 'len cleaned:', len(cleaned_errors) # check that new list size is 90% of the old
    highest_value = cleaned_errors[len(cleaned_errors) - 1]

    def less_than_highest_value(element):


    # --- inefficient way of removing the corresponding points from data ---
    cleaned_data_copy = cleaned_data[:]
    for i in range(len(predictions)):
        isInCleaned = False
        for j in range(len(cleaned_errors)):
            if cleaned_errors[j] == sorted_residual_errors[i]:
                isInCleaned = True
                break
        if not isInCleaned:
            cleaned_data_copy.remove(j)

    cleaned_data = cleaned_data_copy

    print cleaned_data

    return cleaned_data

