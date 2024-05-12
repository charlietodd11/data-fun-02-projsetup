'''This module provides functions for creating a series of project folders'''
#Import dependencies
import pathlib
import time
import os
import statistics
import charlietodd_utils

#creates a folder for each year students took the ACT prep class
def create_folders_for_range(first_class, last_class) -> None:
  int(first_class) == 2005
  int(last_class) == 2024
  for year in range(first_class, last_class+1):
    pathlib.Path(f"{year}").mkdir(exist_ok=True)

#creates a folder for each student in a list
def create_folders_from_list(students) -> None:
  list(students) == ["Charlie", "Alyssa", "Sofia", "Henry", "Kate"]
  for student_input in students:
    pathlib.Path(student_input).mkdir(exist_ok=True)

#creates a folder a list of names with the prefix- "score"
def create_prefixed_folders(students, prefix) -> None:
  list(students) == ["Charlie", "Alyssa", "Sofia", "Henry", "Kate"]
  str(prefix) == "score"
  for student_input in students:
    pathlib.Path(f"{prefix}-{students}").mkdir(exist_ok=True)

#creates a folder every 5 seconds for the set time
def create_folders_periodically(duration_secs,period) -> None:
  start_time = time.time()
  while(time.time()-start_time < duration_secs):
    current_time = time.time()-start_time
    pathlib.Path(f"Folder created at {round(current_time)} second").mkdir(exist_ok=True)
    time.sleep(period)

def main():
  print(f"Byline: {charlietodd_utils}")
  create_folders_for_range(first_class=2005, last_class=2024)
  create_folders_from_list(students=["Charlie", "Alyssa", "Sofia", "Henry", "Kate"])
  create_prefixed_folders(students=["Charlie", "Alyssa", "Sofia", "Henry", "Kate"], prefix="score")
  create_folders_periodically(duration_secs=5, period=1)

if __name__=="__main__":
  main()

  

  
