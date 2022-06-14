def split(string: str, delim: str):
    cur_sec = ""

    i = 0
    while i < len(string):
        if string[i : i + len(delim)] == delim:
            yield cur_sec
            yield delim
            cur_sec = ""
            i += len(delim)
            continue
        cur_sec += string[i]
        i += 1

    yield cur_sec
