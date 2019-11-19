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
    if user_choice == "V":
      if len(calendar.keys()) < 1:
        print "The calendar is empty"
      else:
        print calendar
    elif user_choice == "U":
      date = raw_input("What date ?")
      update = raw_input("Enter the update :")
      calendar[date] = update
      print "Update successful :-)"
      print calendar
    elif user_choice == "A":
      event = raw_input("Enter event : ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if len(date) > 10 or int(date[6:]) < int(strftime("%Y")):
        print "You entered an invalid date !"
        try_again = raw_input("Try again ? Y fpr yes and N for N : ").upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calendar[date] = event
        print "Event added successfully !"
        print calendar
