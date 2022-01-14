def main(fruits):
    """
    A list called "fruits" is given and is five in length and contains at least one "apple". Remove the apples from the list and return the list.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    if fruits.count("apple") > 0:
        idx = fruits.index("apple")
        fruits.pop(idx)
        if fruits.count("apple") > 0: 
            idx = fruits.index("apple") 
            fruits.pop(idx)
            if fruits.count("apple") > 0: 
                idx = fruits.index("apple") 
                fruits.pop(idx)
                if fruits.count("apple") > 0: 
                    idx = fruits.index("apple") 
                    fruits.pop(idx)
                    if fruits.count("apple") > 0:
                        idx = fruits.index("apple") 
                        fruits.pop(idx)
                    
                    else:
                        return fruits
                
                else:
                    return fruits
            
            else:
                return fruits
        
        else:
            return fruits
        
    else:
        return fruits