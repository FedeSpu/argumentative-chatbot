import subprocess as sub
from pathlib import Path
import os

# Save the current working directory for restoring it after running margot
pythonCwd = os.getcwd()
home = str(Path.home())
# Sample.txt will be replaced by the user's input
inputFile = 'sample.txt'
outputDir = 'output/'
# Change current working directory with the margot one, otherwise it doesn't work
os.chdir("../predictor")

print("Start")
p = sub.Popen(['bash', 'run_margot.sh', inputFile, outputDir])
# Wait until bash program has finished
p.communicate()
print("Finish")
