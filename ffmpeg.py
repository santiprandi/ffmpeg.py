#!/usr/bin/env python3

# ffmpeg wrapper with useful commands.
# v0.4
# Recommended Python version: 3.9 or above.
# Only tested on Linux.

# TODO Should I have into account that subprocess.run does not work on python 3.4 or earlier?

import subprocess
import argparse


def main():
    # Create top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="subparser")

    # Other parsers
    gif_to_mp4_parser = subparsers.add_parser(
        "gif-to-mp4", help="optimize a gif for web usage")
    gif_to_mp4_parser.add_argument("input", help="input file name")
    gif_to_mp4_parser.add_argument(
        "output", help="output file name with .mp4 extension")

    extract_audio_parser = subparsers.add_parser(
        "extract-audio", help="extract audio from file without reencoding")
    extract_audio_parser.add_argument("input", help="input file name")
    extract_audio_parser.add_argument("output", help="output file name")

    trim_parser = subparsers.add_parser(
        "trim", help="trim a file without re-encoding")
    trim_parser.add_argument("input", help="input file name")
    trim_parser.add_argument("output", help="output file name")
    trim_parser.add_argument(
        "start", help="the start of the section to trim (HH:MM:SS)")
    trim_parser.add_argument(
        "end", help="the end of the section to trim (HH:MM:SS)")

    nv_parser = subparsers.add_parser(
        "nv", help="tools with NVIDIA transcoder")

    args = parser.parse_args()

    if args.subparser == "gif-to-mp4":
        gif_to_mp4(args)
    elif args.subparser == "extract-audio":
        extract_audio(args)
    elif args.subparser == "trim":
        trim(args)


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


def extract_audio(args):
    subprocess.run(["ffmpeg",
                    "-i", args.input,
                    "-vn",
                    "-acodec", "copy",
                    args.output])
    # -vn - No video.
    # -acodec copy - Use the same audio stream that's already in there.


def trim(args):
    # TODO Improve. Maybe make start and end optional. Add option for duation to trim insted of end time.
    subprocess.run(["ffmpeg",
                    "-i", args.input,
                    "-ss", args.start,
                    "-to", args.end,
                    args.output])
    # -ss HH:MM:SS - It defines the start of the section that you want to
    # trim.

    # -to HH:MM:SS - It's the end of the section that you want to trim.

    # -c copy - This is an option meaning trimming video via stream copy,
    # which is fast and will not re-encode video.

    # -t HH:MM:SS - Instead of -to. It means the duration of the section to trim,
    # rather than the end time.


if __name__ == "__main__":
    main()

# Resources about argparse:
# https://coderzcolumn.com/tutorials/python/argparse-simple-guide-to-command-line-arguments-handling-in-python
# https://docs.python.org/3/howto/argparse.html
# https://docs.python.org/3/library/argparse.html#argparse.ArgumentParser.add_subparsers

# Resources about ffmpeg:
