import argparse

parser = argparse.ArgumentParser(description="simple calcualator")
parser.add_argument("num1", type=float, help="first number")
parser.add_argument("num2", type=float, help="second number")
parser.add_argument("operations", choices=["add","sub","div","mul"] , help="operations")

args = parser.parse_args()
if (args.operations=="add"):
    print(f"sum = {args.num1 + args.num2}")
elif (args.operations=="sub"):
    print(f"sub = {args.num1 - args.num2}")
elif (args.operations=="mul"):
    print(f"mul = {args.num1 * args.num2}")
elif (args.operations=="div"):
    print(f"div = {args.num1 / args.num2}")
else:
    print("Check input")