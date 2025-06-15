# read_yaml 
# https://www.youtube.com/watch?v=fwLBfZFrLgI
# exception, function

def my_Process(first_argument):
    try:
        with open(sys.argv[1], 'r') as file:
            stream = file.read()
            dictionary = yaml.load(stream, Loader=yaml.FullLoader)
            x = datetime.datetime.now() 
            console.print("\n"+x.strftime("%c") + "\n" +"Processing: " + first_argument + "\n")
            for key, value in dictionary.items():
                console.print(key + " : " + str(value))
    except:
        print("An exception occurred")
#-------------------------------------------------------------
import datetime
import sys
import yaml

#Makes the Output pretty
from rich.console import Console
console = Console()

if len(sys.argv) > 1:
  # User provided at least one argument
  my_Process(sys.argv[1])
else:
  # User did not provide any arguments after script name
  print("No YML file specified.")
  sys.exit()

 

