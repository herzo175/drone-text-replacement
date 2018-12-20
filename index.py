import re
import fileinput
import os
import functools


def get_regex(words):
    return r"{}+\s*({})\s*{}+".format(re.escape("{"), "|".join(words), re.escape("}"))


def trim_braces(word):
    start = r"{}+\s*".format(re.escape("{"))
    end = r"\s*{}+".format(re.escape("}"))
    return functools.reduce(lambda s, regex: re.sub(regex, "", s), [start, end], word)


def replace_match(line, match, replacements):
    # find key that matches the group. Fail if word not specified
    word = replacements[trim_braces(match.group(0))]
    return "{}{}{}".format(line[:match.start()], word, line[match.end():])


def replace_line(line, regex, replacements):
    match = re.search(regex, line)

    if match is None:
        return line
    else:
        return replace_line(replace_match(line, match, replacements), regex, replacements)


def replace_file(filename, replacements):
    with fileinput.FileInput(filename, inplace="True") as file:
        # replacements = {"poo": "hello", "pee": "world"}
        regex = get_regex(replacements.keys())

        for line in file:
            print(replace_line(line, regex, replacements), end='')


def main():
    # NOTE: make sources more configurable?
    # NOTE: keys must be uppercase in the target file
    filename = os.environ["PLUGIN_FILENAME"]
    replacements = {
        k.replace("PLUGIN_", ""): os.environ[k]
        for k in os.environ
        if k.startswith("PLUGIN_")
    }

    replace_file(filename, replacements)


if __name__ == "__main__":
    main()