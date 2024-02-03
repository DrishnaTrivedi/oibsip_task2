import argparse
import sys
parser = argparse.ArgumentParser()

parser.add_argument('--w', type=float)
parser.add_argument('--h', type=float)

args = parser.parse_args()
weight = args.w * 2.20462262   #in pounds
height = args.h * 0.39370079   #in inches

if(args.h >=0 and args.w >=0 ):
    bmi=(weight / (height  * height )) * 703
    bmi = round(bmi,3)
    sys.stdout.write(f"Your bmi is {bmi}")
    sys.stdout.write("\n")

    if(bmi <= 18.5):
        sys.stdout.write("YOU ARE UNDERWEIGHT")
    elif(bmi > 18.5 and bmi <= 24.9):
        sys.stdout.write("YOUR BMI FALLS IN THE NORMAL RANGE")
    elif(bmi >24.9 and bmi <=  29.9):
        sys.stdout.write("YOUR BMI FALLS IN THE OVERWEIGHT RANGE")
    else:
        sys.stdout.write("YOUR BMI FALLS IN THE OBESE RANGE")
else:
    sys.stdout.write("ENTER VALID HEIGHTS AND WEIGHTS")