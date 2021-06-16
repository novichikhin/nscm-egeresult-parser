import argparse
from parse import Parser

def main():
    arg_parser = argparse.ArgumentParser(description='NSCM ege result parser')
    arg_parser.add_argument('--lastname', type=str, help='Last name')
    arg_parser.add_argument('--firstname', type=str, help='First name')
    arg_parser.add_argument('--code', type=str, help='Registration code')
    args = arg_parser.parse_args()

    parser = Parser(args.lastname, args.firstname, args.code)
    results = parser.get_results()
    for result in results:
        print(f"{result['subject']} | {result['date']} | {result['score']}")

if __name__ == '__main__':
    main()