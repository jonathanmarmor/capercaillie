#!/usr/bin/env python

from phase import Phase


def main():
    phaser = Phase(
        sample_file_name='capercaillie_sample.wav',
        start_pad_duration=0.024,
        end_pad_duration=0.024)

    phaser.phase(
        output_file_name='output.wav',
        n_tracks=5,
        gap=0.18,
        repeat_count=10,
        end_align=True)


if __name__ == '__main__':
    main()
