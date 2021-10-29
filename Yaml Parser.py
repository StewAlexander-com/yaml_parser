#!/usr/bin/env python3
import os
import sys
import yaml 

#intiial value for key
key = 0 

#This program creates a list of keys from a ingested yaml file,
#and then prints the keys in the list in a new file called "keys.txt"
#Then one can ask for the value of a key by typing the key name in the terminal, which it also
#saves in a yaml file called "outputs.yaml"

print ("\nThis is a Program to parse a yaml file and print the keys in a new file called \"keys.txt\" \n\n")
print ("This program also displays the values of an available key, as well as outputing them to a file")
print ("called outputs.yaml\n\n")

#open a path to the current directory
path = os.path.dirname(os.path.realpath(__file__))
#show the contents of the curent directory
print ("The current directory is: " + path, ",and the list of contents is:\n")
print(os.listdir())
#ask the user to enter the yaml file name in the current path
yaml_file = input("Enter the yaml file name: ")


# while loop to check if the file exists
while True:
    if os.path.isfile(yaml_file):
        print ("Ingesting the file\n")
        break
    else:
        print("File does not exist")
        yaml_file = input("Enter the yaml file name: ")

#import the yaml file and store the contents in a dictionary
with open(yaml_file, 'r') as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)


#pretty print the keys of the dictionary to a file called keys.txt and to the console
with open("keys.txt", "w") as f:
    for key in data:
        f.write(key + "\n")
        print(key)


# loop if the the key is found in the dictionary, othterwise print "key not found" until the user enters "q"
while key != "q":
    print ("\n")
    key = input("Enter the key, or \"q\" to quit: ")
    if key in data.keys():
        #print the value to the sceen in yaml format
        print(yaml.dump(data[key], default_flow_style=False))
        #print in yaml format the key and value to a file called outputs.yaml
        with open(path + "/outputs.yaml", "a") as f:
            f.write(key + ": " + yaml.dump(data[key], default_flow_style=False))
            f.write("\n=====================\n\n")
    else:
        print("Key not found")
        if key == "q":
            print ("Exiting")
            break
        else:
            continue
