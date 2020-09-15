import argparse
from project.utils import ColorConsole as cc
from project import parser


TEST_FILE = './tests/test_files/test1.txt'


def main():

    arg_parser = argparse.ArgumentParser()

    arg_parser.add_argument("-i", "--input_path",
                            help="Completer file path of input file",
                            default=TEST_FILE,
                            type=str)

    arg_parser.add_argument(
        "-d", '--debug', help='Prints out PARSER States and Debug informations.',
        default=False, action='store_true')

    args = arg_parser.parse_args()

    file_path = args.input_path
    debug_ = args.debug

    cc.out(f'[INFO] Input file: {file_path}', cc.YELLOW)

    try:
        with open(file_path, 'r') as input_file:
            contents = input_file.read()
            try:
                parser.parser.parse(input=contents, debug=debug_)

                if parser.parser.errorok is False:
                    # Error
                    raise Exception('Incomplete Syntax')

                cc.out(f'[SUCCESS] Grammar Successfully parsed!',
                       cc.OKGREEN, cc.BOLD)

            except Exception as err:
                cc.out(f'[ERROR]: {err}', cc.FAIL)

    except FileNotFoundError as fileErr:
        cc.out(f'[ERROR] File "{file_path}" not found.', cc.YELLOW)

    return 'true'
