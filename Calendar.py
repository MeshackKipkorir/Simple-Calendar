"""
Simple Command Line calendar program
"""

from time import sleep,strftime

#welcome user function

name = "" #your name goes here
def welcome():
  print "Welcome " + name
  print "*** Calendar is opening"
  sleep(1)
  print "Today is : " + strftime("%A %B %d, %Y")
  print "The time is :" + strftime("%H : %M : %S")
  sleep(1) 
  print "What would you like to do ?"
  
def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("Enter A to Add, U to update,V to view ,D to delete , X to exit :").upper()
