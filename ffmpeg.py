#!/usr/bin/env python3

# ffmpeg wrapper with useful commands.
# v0.1
# Recommended Python version: 3.9 or above.
# Only tested on Linux.

# TODO should i have into account that subprocess.run does not work on python 3.4 or earlier?
# TODO check conflicting options:
# https://docs.python.org/3/howto/argparse.html#conflicting-options

import subprocess
import argparse

arg_parser = argparse.ArgumentParser()
# subprocess.run(["ls", "-l"])
arg_parser.add_argument("action", help="what to do",
                        choices=["gif-to-mp4", "extract-audio", "trim", "nv"])
arg_parser.add_argument("input", help="input file")
arg_parser.add_argument("-o", "--output", help="output file", action="store")

args = arg_parser.parse_args()

print(args)

if args.action == "gif-to-mp4":
    subprocess.run(["ffmpeg", "-i", args.input,
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

# Sources:
# https://coderzcolumn.com/tutorials/python/argparse-simple-guide-to-command-line-arguments-handling-in-python
# https://docs.python.org/3/howto/argparse.html
