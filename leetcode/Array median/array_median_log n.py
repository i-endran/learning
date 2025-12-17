import math

def find_median(A, B):

    m, n = len(A), len(B)

    if (m > n):
        A, B = B, A
        m, n = n, m

    mid_a_l =  m // 2 # taking floor division on length return index + 1, it is intended

    bingo = False

    for _ in range(m+n):

        mid_b_l = ((m + n + 1) // 2 ) - mid_a_l - 2 # reducing the length to index

        #print(str(mid_a_l) + " " + str(mid_b_l))

        if _get_value(A, mid_a_l) <= _get_value(B, mid_b_l + 1) and _get_value(B, mid_b_l) <= _get_value(A, mid_a_l + 1):
            bingo = True
            break

        if _get_value(A, mid_a_l) > _get_value(B, mid_b_l + 1):
            # pull that b_r to left and a_l to right
            mid_a_l -= 1
        else:
            mid_a_l += 1
            
    
    if (bingo):
        if (m + n) % 2:
            return max(_get_value(A, mid_a_l), _get_value(B,mid_b_l))
        else:
            return ( max(_get_value(A, mid_a_l), _get_value(B, mid_b_l)) + min(_get_value(A, mid_a_l + 1), _get_value(B, mid_b_l + 1)) ) / 2
    else:
        return None

        
def _get_value(array, i):
    if i < 0:
        return -9999999
    elif i > len(array) - 1:
        return 9999999
    else:
        return array[i]


def main():
    A = [5,5,5,5,5]
    B = [5,5,5,5,5,5]

    median = find_median(A, B)
    print ("median -> " + str(median))

if __name__ == "__main__":
    main()