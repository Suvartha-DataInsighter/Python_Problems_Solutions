import argparse
parser=argparse.ArgumentParser()

## Working with Positional arguments
# parser.add_argument("square",help='display a square of a given number',type=int)
# args=parser.parse_args()
# print(args.square**2)

## Working with Optional arguments
# parser.add_argument("--verbosity", help="increase output verbosity")
# args = parser.parse_args()
# if args.verbosity:
#     print("verbosity turned on")
# Here is this case --verbosity is expecting any value defaultly,

# parser.add_argument("--verbose", help="increase output verbosity",
#                     action="store_true")
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")
# In the above we need not to mention any expected value ,the action variable will defaultly assigns value to run the code



### Combining the Positional and Optional Arguments which are passed on to command prompt

parser.add_argument("square", type=int,
                    help="display a square of a given number")
parser.add_argument("-v", "--verbose", action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()
answer = args.square**2
if args.verbose:
    print(f"the square of {args.square} equals {answer}")
else:
    print(answer)
