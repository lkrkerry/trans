from fractions import Fraction as Fr
def trans(times, number):
    
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
if __name__ == '__main__':
    a = trans(10, 3.1)
    print(a)
