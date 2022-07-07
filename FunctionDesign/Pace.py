from statistics import mean
import random

#Create and fill list of length N with numbers between 0 and 1
def fill_inst_pace(N):

  inst_pace = []

  for i in range(0, N):
    inst_pace.append(random.random())

  return inst_pace

#For given list inst_pace, generate all contiguous sublists of length sub_dist and
# calculate their averages (i.e. the pace for the smaller distance)
def calc_sub_paces(sub_dist, inst_pace):

  N = len(inst_pace)
  sub_sz = int(N*sub_dist)
  sub_len = int( N - sub_sz)
  sub_pace = [0]*sub_len

  for i in range(0, sub_len-1):
    #All possible sub chunks of length sub_dist
    sub_pace[i] = mean(inst_pace[i:i+sub_sz])

  return sub_pace

#Create a list of instantaneous paces of length N and check that each one has a contigious sub-list
# of fractional length sub_dist such that average(sublist) >= average(whole list)
def create_list_and_check_subsections(N, sub_dist):

  inst_pace = fill_inst_pace(N)

  av_pace = mean(inst_pace)

  sub_pace = calc_sub_paces(sub_dist, inst_pace)

  sub_flags = [s>av_pace for s in sub_pace]
  
  if not True in sub_flags:
    print(av_pace, sub_pace)


  return True in sub_flags


def main():

  # Program to answer the question:
  #  If I run a 10km race at an average pace of 10km/hour, have I definitely also
  #  completed a 5km single stretch at 10km/hour? What about 3km? What about 8km?

  # Simplifications - allow instantaneous pace to be random number between 0 and 1, i.e. average about 0.5
  # If it holds for this, it holds for random variations about an average, and should also hold for systematic ones
  # Ignore the difference between time-average and distance averaged paces
  # Discretise into N time points
  # Use simple averaging instead of integration
  # Express the shorter distance as a fraction of the total

  # Inputs
  N = 500  # Number of time points
  trials = 1000  # Number of repetitions of check
  sub_dist = 0.75  #  Fraction of total distance to investigate

  # How often to print to screen
  display_frac = 100

  # Output - how often our assumption is violated
  fails = 0

  for i in range(trials):
    if i%display_frac == 0: print(i/trials*display_frac, '% done')
    # What comment can I put here that says more than the code does?
    if not create_and_check_subs(N, sub_dist):
      fails = fails+1

  # Check count of failures
  if(fails > 0):
    print("Trial FAILED")
    print(fails/trials*100, " % failed")

if __name__ == "__main__":

  main()




