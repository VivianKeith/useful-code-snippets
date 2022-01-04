import argparse


parser = argparse.ArgumentParser(description = "A simple demo of parameters parser.")
group = parser.add_mutually_exclusive_group()

group.add_argument("-v", "--verbose", action="count", default=0,
                    help="Display output in more details")
group.add_argument("-q", "--quiet", action="store_true",
                    help="Display no more info")
parser.add_argument("-o", "--operation", type=str, choices=["+", "-", "*", "/"],
                    required=True, default="+",
                    help="How to operate the two numbers you passed")

parser.add_argument("p1", type=int,
                    help="The 1st positional parameter")
parser.add_argument("p2", type=int,
                    help="The 2nd positional parameter")

args = parser.parse_args()

if args.operation == "+":
    answer = args.p1 + args.p2
elif args.operation == "-":
    answer = args.p1 - args.p2
elif args.operation == "*":
    answer = args.p1 * args.p2
elif args.operation == "/":
    answer = args.p1 / args.p2

if args.quiet:
    print(f"{answer}")
elif args.verbose >= 2:
    print(f"running {__file__}")
    print(f"The two parameters are: {args.p1}, {args.p2}\n",
            f"The operation is \"{args.operation}\"\n",
            f"The answer is {answer}",
            sep="")
elif args.verbose == 1:
    print(f"The two parameters are: {args.p1}, {args.p2}\n",
            f"The operation is \"{args.operation}\"\n",
            f"The answer is {answer}",
            sep="")
else:
    print(f"{args.p1} {args.operation} {args.p2} = {answer}")

