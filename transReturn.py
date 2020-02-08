

from fractions import Fraction as Fr


def tr(times, number):
    
    print(number)
    p2 = []
    p = number
    print('-'*80)
    if times != 'True':
        try:
            for i in range(times):
                try:
                    p1 = int(p)
                except ValueError:
                    print('please enter number')
                    break
                
                
                p2.append(p1)
                p -= p1
                
                
                try:
                    p = Fr(1/p)
                    
                except ZeroDivisionError:
                    return p2
        except TypeError:
            print('please enter number')
    
    else:
        while 1:
            try:
                    p1 = int(p)
            except ValueError:
                print('please enter number')
                break
            print(p1)
            p -= p1
            try:
                p = Fr(1/p)
            except ZeroDivisionError:
                break
    return p2

def transReturn(return_obj='last', times=10,item=3.1415926,mode=1):
    trans = tr(times, item)
    transr = trans[::-1]
    if return_obj == 'last':
        if mode == 2:
            return transr[0]
        elif mode == 1:
            a = transr[0]
            for i in range(times-1):
                a = Fr(1,a)
                a += trans[i+1]
            return a
        else:
            raise ValueError('Mode should be 1 or 2')
            
            
            
    elif return_obj == 'all':
        if mode == 2:
            return trans
        elif mode == 1:
            b = trans[0]
            for i in range(times-1):
                for j in range(i+1):
                    b = Fr(1,b)
                    b += trans[j+1]
                    print(b)
            return None
        else:
            raise ValueError("return_obj should be 'last' or 'all'" )


if __name__ == "__main__":
    a = transReturn()
    print(a)
