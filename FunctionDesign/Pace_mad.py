from statistics import mean
import random

def do_things(N, sub_dist):

  inst_pace = []

  for i in range(0, N):
    inst_pace.append(random.random())


  sub_sz = int(N*sub_dist)
  sub_len = int( N - sub_sz)
  all_sub_pace = []

  # Create all the possible sub chunks of length sub_dist
  for i in range(0, sub_len-1):
    #All possible sub chunks of length sub_dist
    all_sub_pace.append(inst_pace[i:i+sub_sz])

  # Get overall average
  av_pace = mean(inst_pace)

  # Check all subs against average
  answer = True in [mean(s)>av_pace for s in all_sub_pace]

  # BLAM - reduce all that to a single answer

  return answer


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
  sub_dist = 0.5  #  Fraction of total distance to investigate

  # How often to print to screen
  display_frac = 100

  # Output - how often our assumption is violated
  fails = 0

  for i in range(trials):
    if i%display_frac == 0: print(i/trials*display_frac, '% done')
    # What comment can I put here that says more than the code does?
    if not do_things(N, sub_dist):
      fails = fails+1

  # Check count of failures
  if(fails > 0):
    print("Trial FAILED")
    print(fails/trials*100, " % failed")

if __name__ == "__main__":

  main()




