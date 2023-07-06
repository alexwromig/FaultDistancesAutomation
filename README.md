# FaultDistancesAutomation
Python script to automate fault distances conversion to miles
============================CONTENTS================================
FD.ipynb - Jupyter Notebook version of script, clearer for beginners
FD.py - Python script version, runs to completion in terminal

==============================SETUP=================================
INSTALL PYTHON!! 
The script requires the python language to run, which you must install first.

Install Python using the below link:

https://www.python.org/downloads/

I like to use Anaconda help organize my python environments.

1. Follow the below instructions to set up Anaconda on your computer:
 
   https://docs.anaconda.com/free/anaconda/install/windows/

2. Once you're finished installing, search for Anaconda Prompt (looks like a black box) and open it.

3. Create a new conda environment for the Fault Distances script with the below line:

    conda create --name FD pandas
 
   then hit enter. "FD" is the name of the environment, so if you want to give the environment a different name you can change that part to whatever you want.
 
   Pandas is one of the modules we'll need to run the script.

5. The below prompt will show up:
 
   Proceed ([y]/n)? y
 
   type y then enter. The environment will be created.

6. Now that the environment has been created, you can activate it by entering:

   conda activate FD

7. We can install jupyter notebook in the environment by entering:

   conda install notebook

   This is only necessary if you want to use the notebook version of the script.

   I recommend using this version of the script if you're new to python/coding.

=============================HOW TO RUN===============================
FOR JUPYTER NOTEBOOK:

1. Run Anaconda Prompt

2. Activate the Fault Distances environment with the following line:

   conda activate FD

3. Enter the following line:

   jupyter notebook

4. The jupyter notebook file explorer should open up on your browser.

   Go to the folder containing the script and open it, then click Run at the top of the page

   Run will run a single segment of code, so you'll have to click run for each segment of code (called cells)

5. If done properly, you'll have a table that will print at the bottom. Copy the table and replace the existing fault distances table in your text file.

FOR PYTHON:

1. Run Anaconda Prompt

2. Activate the Fault Distances environment with the following line:

   conda activate FD

3. Navigate to the folder containing the python file by entering the following:

   cd <filepath>

   Replace <filepath> with the location of the folder.

   If you're having trouble finding the file path, right click on the folder in your File Explorer, go to Properties, and copy the Location.

   It should looks something like C:\Users\blahblahblah

4. Enter the following into the Anaconda Prompt:

   python FD.py

5. It should prompt you to open a file. Select the fault distances text file you want and it should output a table for you.

7. Copy and paste that table into the text file.
