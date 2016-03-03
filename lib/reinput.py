#! /usr/bin/python3
# -*- coding:utf-8 -*-

"""
My version of input.
"""

def reinput(prompt, prompt_end = ": ",
        valid = None, default = None, type=str, func=input, **kw):
    """Print the prompt and wait for inputs from the user until this
    input is valid. If the input is empty, default is returned (if
    given).
    """

    cin = None

    # Replace '\t' with space
    prompt = prompt.replace('\t', ' '*4)

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
            cin = func(prompt, **kw)
    elif default:
        cin = func(prompt, **kw)
    else:
        while cin in ['', None]:
            cin = func(prompt, **kw)

    # Return the default value if required
    if default and cin == '':
        return default
    else:
        return type(cin)

if __name__ == '__main__':
    # Basic usage
    cin = reinput("Six fois sept font...", default=42, type=int)
    print("Vous avez dit %d ?" % cin)

    # Now, with cinput
    from cinput import cinput
    valid_numbers = ['quatre', 'vingt', 'quarante-deux', 'un']

    cin = reinput("Quel est le nombre après deux ?",
            default="huit", valid=valid_numbers, func=cinput,
            complete = valid_numbers)
    print("Vous avez dit %s ?" % cin)

