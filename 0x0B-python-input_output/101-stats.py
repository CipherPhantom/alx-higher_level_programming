#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics."""
import sys


file_size = 0
stats = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
}

try:
    count = 0
    for line in sys.stdin:
        count += 1
        info = line.split()
        file_size += int(info[-1])
        stats[info[-2]] += 1

        if count % 10 == 0:
            stats_text = ""
            stats_text += f"File size: {file_size}\n"
            for key, value in stats.items():
                if value > 0:
                    stats_text += f"{key}: {value}\n"
            print(stats_text, end="")

except KeyboardInterrupt:
    stats_text = ""
    stats_text += f"File size: {file_size}\n"
    for key, value in stats.items():
        if value > 0:
            stats_text += f"{key}: {value}\n"
    print(stats_text, end="")
