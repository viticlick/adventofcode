
def elevator(text):
    open_parenthesis = text.count('(')
    close_parenthesis = text.count(')')
    return open_parenthesis - close_parenthesis

def basement(text):
    current_position = 0;
    count = 0 
    for value in text:
        count = count + 1
        if value == '(':
            current_position = current_position + 1
        if value == ')':
            current_position = current_position - 1
        if current_position == -1:
            return count 
