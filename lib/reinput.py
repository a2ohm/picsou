#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
My version of input.
"""

def reinput(prompt, prompt_end = ": ",
        valid = None, default = None, type=str):
    """Print the prompt and wait for inputs from the user until this
    input is valid. If the input is empty, default is returned (if
    given).
    """

    cin = None

    # If a default value is given, print it at the end of the prompt
    if default:
        prompt += " [%s] %s" % (str(default), prompt_end)

        # If a default value is given, the empty string becomes a valid
        # input.
        if valid:
            valid += ['']
    else:
        prompt += prompt_end


    # Get the input
    if valid:
        while cin not in valid:
            cin = input(prompt)
    else:
        cin = input(prompt)

    # Return the default value if required
    if default and cin == '':
        return default
    else:
        return type(cin)
