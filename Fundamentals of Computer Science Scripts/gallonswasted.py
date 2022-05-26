# Welcome to the Gallons Wasted Calculator. With this calculator, a user can discover exactly how
# much water they waste by leaving their faucet on for a certain amount of days).
# The calculations are all based off of the fact that there are 15,140 faucet drips per gallon according
# to the US Geological Service website.

DRIPS_PER_GALLON = float(15140)
MINUTES_IN_A_DAY = float(1440)

print("How many drips per minute?")
dripsPerMinute = float(input())

print("How many days?")
numberOfDays = float(input())

totalMinutes = numberOfDays * MINUTES_IN_A_DAY
totalDrips = totalMinutes * DRIPS_PER_MINUTE
totalGallons = totalDrips / DRIPS_PER_GALLON

print("")
print(f"If a faucet has {dripsPerMinute} drips per minute for {numberOfDays} days, the faucet will waste {totalGallons} gallons of water.")