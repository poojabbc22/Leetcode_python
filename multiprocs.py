import multiprocessing
def print_cube(num):
    print("the area of a cube {}".format(num*num*num))
def print_square(num):
    print("the rea of square {}".format(num*num))
if __name__=="__main__":
    p1=multiprocessing.Process(target=print_square,args=(4,))
    p2=multiprocessing.Process(target=print_cube,args=(5,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("done")