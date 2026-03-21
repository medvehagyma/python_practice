# Ages decision pattern example
## User documentation


### About the program
I'm learning the decision pattern in Python and this is an example using persons from various ages.  
There are persons' names and ages in a list and I'm deciding if there exists anyone above 28.

### How to start the program
To use this program one needs to have Python on their computer.  
Then you may run the program from a terminal.  
There are 3 ways to run the program:  
- using a hard-coded dataset inside of the program  
- entering the data into the program from the keyboard  
- reading the data from a file in the `data` folder   

To use the hard-coded dataset run the following command in the terminal:  
` py ages.py `  

To enter the data from the keyboard run the following command in the terminal:  
` py ages.py keyboard `  
In this mode you will be prompted first to enter the count of persons that you will processing with the algorithm.  
Then you will be prompted to enter the names and ages of each person one by one.

To read the data from a file run the following command in the terminal:  
` py ages.py <file_name.txt> `   
_`file_name.txt` should be an existing file name of your choice in the `data` folder_   
The input files are expected to have the following structure: each line contains the data of a single person: `<name>;<age>`  
In this format where the name and age are separated by a ;  


## Developer documentation

### About the program
The program was made Python 3.13.2. With Visual Studio Code on Windows 10. The source code is divided into 3 main parts. In order:  
1. inputs 
2. algorithm  
3. outputs  



