#
# Mate Somoracz, Zeiss Assignment, October 2023
#


def read_data_until_end_line(lines, end_line_text=None):
    read_lines = []
    for line in lines:
        if not line:
            continue
        if end_line_text and end_line_text in line:
            break
        read_lines.append(line)

    return read_lines


def read_in_chunks_with_skip(string, chunk_size, skip_size):
    if chunk_size == 0 and skip_size == 0:
        raise AttributeError("Can not read empty chunks with zero skips.")

    i = 0
    while i < len(string):
        chunk = string[i : i + chunk_size]
        yield chunk
        i += chunk_size + skip_size
