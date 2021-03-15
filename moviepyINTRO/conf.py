import os
#tempPath = os.getcwdb()
#print(tempPath)
'''
'''
ABS_PATH = os.path.abspath(__file__)
#print(ABS_PATH)
BASE_DIR = os.path.dirname(ABS_PATH)
#print(BASE_DIR)
DATA_DIR = os.path.join(BASE_DIR, "data")
#print(DATA_DIR)
SAMPLE_DIR = os.path.join(DATA_DIR, "samples")
#print(SAMPLE_DIR)
SAMPLE_INPUTS = os.path.join(SAMPLE_DIR, "inputs")
#print(SAMPLE_INPUTS)
SAMPLE_OUTPUTS = os.path.join(SAMPLE_DIR, "outputs")
#print(SAMPLE_OUTPUTS)