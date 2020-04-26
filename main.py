import threading as th
import pandas as pd
import serial as tx
import datetime
arduino = tx.Serial('/dev/ttyUSB0',9600)


def process_command(command):
    if command == "see":
        print("hardware is fine")


def update_table():
    old_file = pd.read_excel("data.xlsx")
    data = str(arduino.readline())[2:-3]
    data = data.split("-")
    data.insert(0,datetime.datetime.now())
    col =["time", "voltage", "current", "power", "Servo 1", "Servo 2"]
    data = pd.DataFrame([pd.Series(data, index = col)])
    new_file = pd.concat([old_file, data], ignore_index=1)
    new_file.to_excel("data.xlsx", index=False)
    print(new_file)
    return 1
    
    

"""


#SHELL
ID = "ST_101"
while 1:
    command = input(ID, ">>")
    process_command(command)
    
"""


