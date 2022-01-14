def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    counter = fruits.count("apple")
    answer = [counter]
    
    if fruits[0] == 'apple':
        answer.append(0)
    
    if fruits[1] == 'apple':
        answer.append(1)
    
    if fruits[2] == 'apple':
        answer.append(2)
    
    if fruits[3] == 'apple':
        answer.append(3)
    
    if fruits[4] == 'apple':
        answer.append(4)
        
    return answer