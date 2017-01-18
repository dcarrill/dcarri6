import datetime
import platform

print ("dcarri6@uic.edu")

full_name = ["diana", "carrillo", "garcia"]

print (full_name)

i = datetime.datetime.now()

print("%s" %i)

nums = []

def four (start, stop, step):
    while start < stop:
      nums.append(start)
      start+= step
four(17, 40, 6)
print(nums)
print(platform.python_version())

