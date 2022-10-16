import numpy as np

def calculateDistributionOfCustomersByGroup (nCustomers, nFirstId = 0):
    groupSizes = np.zeros (64)
    for i in range(nFirstId, nCustomers):
        groupNumber = sum(map(int,str(i)))
        groupSizes [groupNumber] += 1

    return groupSizes




