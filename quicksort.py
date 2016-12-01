import argparse

def core_quicksort( array ) :
    # basecase : when the size of array is less than 1, nothing to sort
    if len(array) <= 1 : 
        return array
    else : 
        # select pivot
        pvt = array[len(array)/2]
        left = []
        mid = []
        right = []
        for x in array : 
            if x < pvt : 
                left += [x]
            elif x > pvt : 
                right += [x]
            else : 
                mid += [pvt]
        # recursion
        return core_quicksort(left) + mid + core_quicksort(right)


def quicksort( filename ) : 
    f = open(filename, 'r')
    numarr = []
    for line in f : 
        for strnum in line.split() :
            numarr += [int(strnum)]
    print "before sort :"
    print numarr
    numarr = core_quicksort(numarr)
    print "after sort :"
    print numarr
    return
    

if __name__ == "__main__" : 
    parser = argparse.ArgumentParser(description="Process input integers.")   
    parser.add_argument('inputfile', metavar='FILE', help="Input file containing the numbers to be sorted")
    args = parser.parse_args()
    if args.inputfile == '' : 
        # no input number, exit
        print "Input file required, exit"
        sys.exit()
    else : 
        # execute quicksort with the filename
        quicksort( args.inputfile )
	
   
