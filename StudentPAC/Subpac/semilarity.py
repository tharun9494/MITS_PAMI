from PAMI.frequentPattern.basic import FPGrowth as alg
import pandas as pd

# Specify the input parameters
inputFile = 'Transactional_T10I4D100K (2).csv'
separator = '\t'
minimumSupportCountList = [100, 150, 200, 250, 300]

# Initializing an empty DataFrame to store the results
result = pd.DataFrame(columns=['algorithm', 'minSup', 'patterns', 'runtime', 'memory'])

# Iterating over each minimum support count
for minSupCount in minimumSupportCountList:
    # Initializing the FPGrowth algorithm
    obj = alg.FPGrowth(inputFile, minSup=minSupCount, sep=separator)
    # Starting the mining process
    obj.mine()
    # Storing the results in the DataFrame
    result = pd.concat([result, pd.DataFrame({'algorithm': 'FPGrowth', 'minSup': minSupCount,
                                              'patterns': len(obj.getPatterns()), 'runtime': obj.getRuntime(),
                                              'memory': obj.getMemoryRSS()}, index=[0])], ignore_index=True)

# Printing the result
print(result)