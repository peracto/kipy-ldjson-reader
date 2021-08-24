import json
from json import JSONDecodeError
import re

_leading_space_regex = re.compile(r'\S', re.MULTILINE)


def ldjson(stream, buffer_size=64*1024):
    """
    Iterates through each json document in a stream.

    :param stream:
    :param buffer_size:
    """
    buffer = ""
    decoder = json.JSONDecoder()
    error_position = -1
    exception = None

    while True:
        index = 0
        block = stream.read(buffer_size)

        if not block:  # If end of stream
            if exception:  # If end of stream and exception, then rethrow it
                raise exception
            break  # otherwise exit

        buffer = buffer + block
        buffer_len = len(buffer)
        exception = None

        try:
            while True:
                # We looks for the first non-whitespace character
                m = _leading_space_regex.search(buffer, index)

                # If there is no match - then we have only whitespace
                if m is None:
                    buffer = ''
                    break

                index = m.start()

                # if we've move beyond the end of the buffer, then there's nothing to evaluate
                if index >= buffer_len:
                    buffer = ''
                    break  # Read next block

                val, index = decoder.raw_decode(buffer, index)
                error_position = -1

                yield val

        except JSONDecodeError as ex:
            # If error is same position as previous error, then it's a physical error
            if ex.pos == error_position:
                raise ex

            exception = ex
            error_position = ex.pos

            if index > 0:
                buffer = buffer[index:]
