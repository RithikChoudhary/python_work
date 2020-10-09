# textwrap is use to wrap the text
import textwrap

def wrap(string, max_width):
    # textwrap.TextWrapper(width=max_width) it is use to define the wrapper ..what to do  
    wrapper = textwrap.TextWrapper(width=max_width)
    wraping = wrapper.wrap(text=string)
    # for i in wraping:
    # return ',\n'.join(str(wraping).split(','))
    return '\n'.join(wraping)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)