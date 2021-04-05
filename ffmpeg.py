#!/usr/bin/env python3

# ffmpeg wrapper with useful commands.
# v0.2
# Recommended Python version: 3.9 or above.
# Only tested on Linux.

# TODO should i have into account that subprocess.run does not work on python 3.4 or earlier?

import subprocess
import argparse


def main():
    # create top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser")

    # other parsers
    gif_to_mp4_parser = subparsers.add_parser(
        "gif-to-mp4", help="optimize a gif for web usage")
    gif_to_mp4_parser.add_argument("input", help="input file name")
    gif_to_mp4_parser.add_argument("output", help="output file name")

    extract_audio_parser = subparsers.add_parser(
        "extract-audio", help="extract audio from file without reencoding")

    trim_parser = subparsers.add_parser(
        "trim", help="trim a file without re-encoding")

    nv_parser = subparsers.add_parser(
        "nv", help="tools with NVIDIA transcoder")

    args = parser.parse_args()

    print(args)

    # parser.add_argument("input", help="input file")
    # parser.add_argument(
    #     "-o", "--output", help="output file", action="store")

    if args.subparser == "gif-to-mp4":
        gif_to_mp4(args)


def gif_to_mp4(args):
    subprocess.run(["ffmpeg",
                    "-i", args.input,
                    "-movflags", "faststart",
                    "-pix_fmt", "yuv420p",
                    "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
                    args.output])
    # -movflags – This option optimizes the structure of the MP4 file so the browser
    # can load it as quickly as possible.

    # -pix_fmt – MP4 videos store pixels in different formats. We include this option
    # to specify a specific format which has maximum compatibility across all
    # browsers.

    # -vf – MP4 videos using H.264 need to have a dimensions that are divisible by 2.
    # This option ensures that’s the case.


if __name__ == "__main__":
    main()

# Resources:
# https://coderzcolumn.com/tutorials/python/argparse-simple-guide-to-command-line-arguments-handling-in-python
# https://docs.python.org/3/howto/argparse.html
