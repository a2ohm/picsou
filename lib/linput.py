#! /usr/bin/python3
# -*- coding:utf-8 -*-

def linput(prompt, prompt_end = ": ",
        valid = None, type=str, func=input, **kw):
    """Print the prompt and wait for valid inputs from the user until
    this input is empty. Then a list a all inputs is returned.
    """

    cin = None
    inputs = []

    # Replace '\t' with spaces
    prompt = prompt.replace('\t', ' '*4)
    prompt += prompt_end

    if valid:
        valid += ['']

        while cin != '':
            cin = None
            while cin not in valid:
                cin = func(prompt, **kw)

            if cin == '':
                break
            else:
                inputs += [type(cin)]
    else:
        while cin != '':
            cin = type(func(prompt, **kw))

            if cin != '':
                inputs += [cin]
            else:
                break

    return inputs

if __name__ == '__main__':
    cin = linput("Tags", valid = ['a', 'b', 'c'])
    print(cin)

    # Now with cinput
    from cinput import cinput
    valid_letters = ['a', 'b', 'c']

    cin = linput("Tags",
            valid=valid_letters, func=cinput, complete=valid_letters)
    print(cin)
