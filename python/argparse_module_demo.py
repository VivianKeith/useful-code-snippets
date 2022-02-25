"""A simple argparse module demo
Usage: python argparse_module_demo.py -h
"""
import argparse

parser = argparse.ArgumentParser(description = "A simple demo of parameters parser.")
# add_mutually_exclusive_group() 可以创建一个参数组，在这个组里的参数只允许指定一个，同时指定多个会报错。
group = parser.add_mutually_exclusive_group()
# action="count" 可以依照传入此参数的个数进行不同动作，一般适用于显示不同详细程度的说明信息
group.add_argument("-v", "--verbose", action="count", default=0,
                    help="Display output in more details")
# action="store_true" 可以依照是否传入了此参数进行不同动作
group.add_argument("-q", "--quiet", action="store_true",
                    help="Display no more info")
# required=True 指定此参数必须传入
parser.add_argument("-o", "--operation", type=str, choices=["+", "-", "*", "/"],
                    required=True, default="+",
                    help="How to operate the two numbers you passed")
# 两个位置参数，调用 add_argument() 添加参数的顺序决定了传入的位置参数的顺序 
parser.add_argument("p1", type=int,
                    help="The 1st positional parameter")
parser.add_argument("p2", type=int,
                    help="The 2nd positional parameter")
# 解析所有设置的参数
args = parser.parse_args()

# 参数处理逻辑
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

