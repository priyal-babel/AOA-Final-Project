#!/usr/bin/env python3
import sys

def generate_string(base, indices):
    s = base
    for idx in indices:
        # idx is expected to be 0-based insertion index after which we insert the current string
        # If idx is larger than current last index, this will append at the end (safe)
        insert_pos = min(idx + 1, len(s))  # position in Python slicing
        s = s[:insert_pos] + s + s[insert_pos:]
    return s

def read_input_file(filename):
    with open(filename, "r", newline='') as f:
        # read all lines, strip whitespace, ignore empty lines
        raw_lines = [line.strip() for line in f.readlines()]
    lines = [l for l in raw_lines if l != ""]

    if len(lines) < 2:
        raise ValueError("Input too short. Need at least one base string and one index/second base.")

    # first line is base string s0
    s0 = lines[0]

    # parse indices for s0 until we hit a non-integer (the next base string)
    s_indices = []
    idx = 1
    while idx < len(lines):
        try:
            val = int(lines[idx])
            s_indices.append(val)
            idx += 1
        except ValueError:
            # this line is not an integer -> it's the second base string
            break

    if idx >= len(lines):
        raise ValueError("Missing second base string (t0).")

    # the line at idx is t0
    t0 = lines[idx]
    idx += 1

    # remaining lines should be integer indices for t0
    t_indices = []
    while idx < len(lines):
        try:
            val = int(lines[idx])
            t_indices.append(val)
        except ValueError:
            raise ValueError(f"Unexpected non-integer line where index expected: '{lines[idx]}'")
        idx += 1

    return s0, s_indices, t0, t_indices

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 string_gen.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    try:
        s0, s_indices, t0, t_indices = read_input_file(input_file)
    except Exception as e:
        print("Error reading input:", e)
        sys.exit(2)

    s_final = generate_string(s0, s_indices)
    t_final = generate_string(t0, t_indices)

    with open("actual_input.txt", "w") as out:
        out.write(s_final + "\n")
        out.write(t_final )

if __name__ == "__main__":
    main()
