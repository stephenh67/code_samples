import argparse
import sys
import math


def diff(principal, periods, interest):
    interest = float(interest / (12 * 100))
    total_payout = 0
    for index in range(1, int(periods) + 1):
        diff_payment = math.ceil((principal / periods) + interest * (principal - ((principal * (index - 1)) / periods)))
        print(f'Month {index}: paid out {diff_payment}')
        total_payout += diff_payment
    print()
    print(f'Overpayment = {round(total_payout - principal)}')


def annui(principal, periods, interest):
    interest = float(interest / (12 * 100))
    annuity = math.ceil(principal * (interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))
    print(f'Your annuity payment = {annuity}!')
    print(f'Overpayment - {int(annuity * periods - principal)}')


def princ(interest, periods, payment):
    interest = float(interest) / (12 * 100)
    principal = payment / ((interest * ((1 + interest) ** periods)) / (((1 + interest) ** periods) - 1))

    print(f"Your credit principal = {math.floor(principal)}!")
    print(f'Overpayment - {math.ceil(payment * periods - principal)}')


def peri(principal, payment, interest):
    interest = float(interest) / (12 * 100)
    periods = math.log((payment / (payment - interest * principal)), (1 + interest))
    periods = math.ceil(periods)
    years = periods // 12
    months = periods % 12
    if periods % 12 == 0 and periods != 12:
        print(f"You need {years} years to repay this credit!")
        print("Overpayment =", (periods * payment) - principal)
    elif periods > 12:
        print(f"You need {years} years and {months} months to repay this credit!")
        print("Overpayment =", (periods * payment) - principal)
    elif periods < 12:
        print(f"{months} months")
        print("Overpayment =", (periods * payment) - principal)
    else:
        print("1 year")
        print("Overpayment =", (periods * payment) - principal)


parser = argparse.ArgumentParser()
parser.add_argument("--principal", type=float, help="principal")
parser.add_argument("--interest", type=float, help="interest")
parser.add_argument("--periods", type=float, help="periods")
parser.add_argument("--payment", type=float, help="payment")
parser.add_argument("--type", type=str, help="type")
args = parser.parse_args()

if len(sys.argv) == 5:

    if args.type == "annuity":
        if args.principal is None and args.interest is not None and args.periods is not None and args.payment is not None:
            princ(args.interest, args.periods, args.payment)
        elif args.principal is not None and args.interest is not None and args.periods is None and args.payment is not None:
            peri(args.principal, args.payment, args.interest)
        elif args.principal is not None and args.interest is not None and args.periods is not None and args.payment is None:
            annui(args.principal, args.periods, args.interest)
        else:
            print("Incorrect parameters.")

    elif args.type == "diff" and args.interest is not None:
        diff(args.principal, args.periods, args.interest)

    else:
        print("Incorrect parameters1.")

else:
    print("Incorrect parameters2.")
