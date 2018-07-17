import argparse
import json
import os.path

from .basic_data_provider import list_providers, get_provider
from .tex_gen import tex_gen
from sys import stdin


# TODO: добавить аргументы для настройки компиляции и генерации данных
def get_args():
    parser = argparse.ArgumentParser(
        description='lxgen is a simple command line tool for generating pdf documents from LaTeX templates')
    parser.add_argument('-o', '--output', help='path to resulting pdf', default=None)
    parser.add_argument('-p', '--provider', help='data provider id', choices=list_providers(), default=None)
    parser.add_argument('-t', '--template', required=True, help='path to LaTeX template')
    parser.add_argument('-i', '--input', help='path to input json file', default=None)
    parser.add_argument('-e', '--executable', required=True, help='path to provider executable')
    parser.add_argument('-f', '--export_folder', help='path to export directory', default=os.path.abspath('.'))
    return parser.parse_args()


def main():
    args = get_args()
    input_data = json.load(stdin if args.input is None else open(args.input, 'r'))
    provider = get_provider(args.provider, args.executable)
    data = provider(args.export_folder, input_data)
    tex_gen(args.template, args.output, data)
