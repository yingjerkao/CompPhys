def tree(list):
        n = len(list)
        if n == 0:
            return []
        i = n / 2
        return [ list[i],tree(list[:i]), tree(list[i+1:])]
                    
