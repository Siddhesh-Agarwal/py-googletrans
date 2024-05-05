#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from pygoogletrans import Translator


def main():
    parser = argparse.ArgumentParser(
        description="Python Google Translator as a command-line tool"
    )
    parser.add_argument("text", help="The text you want to translate.")
    parser.add_argument(
        "-d",
        "--dest",
        default="en",
        help="The destination language you want to translate. (Default: en)",
    )
    parser.add_argument(
        "-s",
        "--src",
        default="auto",
        help="The source language you want to translate. (Default: auto)",
    )
    parser.add_argument("-c", "--detect", action="store_true", default=False, help="")
    args = parser.parse_args()
    translator = Translator()

    if args.detect:
        result = translator.detect(args.text)
        result = """
[{lang}, {confidence}] {text}
        """.strip().format(
            text=args.text, lang=result.lang, confidence=result.confidence
        )
        print(result)
        return

    result = translator.translate(args.text, dest=args.dest, src=args.src)
    result = """
[{src}] {original}
    ->
[{dest}] {text}
[pron.] {pronunciation}
    """.strip().format(
        src=result.src,
        dest=result.dest,
        original=result.origin,
        text=result.text,
        pronunciation=result.pronunciation,
    )
    print(result)


if __name__ == "__main__":
    main()
