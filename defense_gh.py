# Author: Chirag Ganguli
# Title: Defense Approach Metric Comparison Chart

from cProfile import label
from random import gammavariate
from random import seed
import json
from PythonLibraries import traceanalyzer as tr
import os
import time
import matplotlib.pyplot as plt


begin = time.time() # SOC

files = os.listdir(".")
AttackOutput = {}
NormalOutput = {}
node_to_check = 5   # node_to_study = 1-7

with open('Attack_Output.json', 'r') as fA:
    AttackOutput = json.load(fA)
    node_to_check = 5

with open('Normal_Output.json', 'r') as fB:
    NormalOutput = json.load(fB)

with open('Defense_Output.json', 'r') as fC:
    DefenseOutput = json.load(fC)

files = os.listdir(".")

# Calculating Average Throughput of the nodes
def AverageTP(node, start, end):
    AvgTP = 0
    for i in range(start, end):
        AvgTP += node['TP'][i]
    AvgTP = AvgTP/(end-start)

    return AvgTP

def AverageED(node, start, end):
    AvgED = 0
    for i in range(start, end):
        AvgED += node['E2EDelay'][i]
    AvgED = AvgED/(end-start)

    return AvgED

def AveragePDR(node, start, end):
    AvgPDR = 0
    for i in range(start, end):
        AvgPDR += node['PDR'][i]
    AvgPDR = AvgPDR/(end-start)

    return AvgPDR

pdr_values = {}
lowest_pdr_values = {}

def find_lowest_pdr_node(data):
    """
    This function takes a dictionary as input and returns the lowest value,
    ignoring any values that are 0.
    
    Parameters:
    data (dict): A dictionary where the values are numerical.
    
    Returns:
    float: The lowest value in the dictionary that is not 0, or None if all values are 0.
    """
    # Filter out values that are 0
    filtered_values = [value for value in data.values() if value != 0]
    
    # Ensure there are values left after filtering
    if not filtered_values:
        return None
    
    # Use the min() function to find the lowest value in the filtered list
    lowest_value = min(filtered_values)
    
    return lowest_value

# Initialize the figure and axis for the plot outside the function to allow multiple calls
fig, ax = plt.subplots()

def selMalNode(node, AvgPDR, start, end, node_to_check, scenario):
    # Node 0-2 : Routers
    # Node 3-7 : Switches
    total = 0
    total1 = 0
    total2 = 0
    data = {}
    seed(1)
    param = [] 
    param1 = []
    param2 = []
    randomMetric = gammavariate(2, 1)
    # Each employed bee generates a new candidate solution in the neighborhood of its present position as equation below:
    for i in range(start, end):
        pdr_values[i] = node['PDR'][i]  / AvgPDR

    print("pDR",pdr_values)
    print("node",node_to_check)
    # print(pdr_values[node_to_check])
    if(node_to_check != 0):
        print("in not 0")
        lowest_pdr_values[node_to_check] = (find_lowest_pdr_node(pdr_values))
        print("lowest",lowest_pdr_values)

    return total2

def printAttackPoint(flag):
    print("[!] Checking Point of Attack at Node " + flag + "...")

def showThroughput(node_to_check):
    # Show the throughput value and graph
    print("Throughput response")

if __name__ == '__main__':
    print("\n")
    print(" == Node Summary == ")
    print("\n")
    # time.sleep(2)
    print(" -- Node 0 --> Router 1 -- ")
    print(" -- Node 1 --> Router 2 -- ")
    print(" -- Node 2 --> Router 3 -- ")
    print(" -- Node 3 --> Switch 1 -- ")
    print(" -- Node 4 --> Switch 2 -- ")
    print(" -- Node 5 --> Switch 3 -- ")
    print(" -- Node 6 --> Switch 4 -- ")
    print(" -- Node 7 --> Switch 5 -- ")
    print("\n")
    # time.sleep(2)
    
    print("\n")
    print(" [*] Defining Metric Composition ")
    print("\n")

    normalSum = 0.0
    attackSum = 0.0
    defenseSum = 0.0
    flag = 0
    valN = {}
    valA = {}
    valD = {}
    valNm = []
    valAt = []
    valDf = []
    isfit = []
    fit = {}
    fitnessSum = 0.0

    
    for node in range(0,8):
        start = 0
        end = 7

    print("\n")
    # time.sleep(2)
    print(" [*] Generating PDR Visuals ")
    print("\n")
    # time.sleep(2)
    showThroughput(str(node_to_check))

    print("\n")
    print(" [*] Dislaying Parametric Graph corresponding to each Node ")
    print("\n")
    # time.sleep(2)
    Normaldictionary = json.load(open('Normal_Output.json', 'r'))
    Attackdictionary = json.load(open('Attack_Output.json', 'r'))
    DefenseDictionary = json.load(open('Defense_Output.json', 'r'))
    NxAxis = [key for key, value in Normaldictionary.items()]
    NyAxis = [value for key, value in Normaldictionary.items()]
    AxAxis = [key for key, value in Attackdictionary.items()]
    AyAxis = [value for key, value in Attackdictionary.items()]
    DxAxis = [key for key, value in DefenseDictionary.items()]
    DyAxis = [value for key, value in DefenseDictionary.items()]

    print(lowest_pdr_values)

plt.show()

end = time.time() # EOC
print("\n")
print(f"Code executed in {end - begin}s")
# time.sleep(2)
print("\n == End of Program ==")
print("\n")

try:
    del tr
    del files
    del node_to_check
    del normalSum
    del attackSum
    del flag
    del start
    del end
    del AverageTP
    del AverageED
    del AveragePDR
    del selMalNode
    del begin
    del end
    del time
except Exception:
    pass