def compress(source):
    return process(source, 1, source[0], 1)


def process(source, index=0, buffer='', count=1):
    return (
        persist(source, index, buffer, count)
        if index < len(source)
        else buffer
    )


def persist(source, index, buffer, count):
    return (
        process(source, index + 1, buffer, count + 1)
        if source[index] == buffer[-1]
        else process(source, index + 1, append(buffer, source[index], count), 1)
    )


def append(buffer, char, count):
    return buffer + ('' if (count < 2) else str(count)) + char
