import pyramid  

def main():
    print("Evaluate get_height function")
    assert(pyramid.get_height(0) == 0)
    assert(pyramid.get_height(1) == 1)
    assert(pyramid.get_height(2) == 1)
    assert(pyramid.get_height(3) == 2)
    assert(pyramid.get_height(7) == 3)
    assert(pyramid.get_height(10) == 4)
    assert(pyramid.get_height(16) == 5)

    ## Optional challenge, uncomment to test
    print("Evaluate get_max_blocks function")
    assert(pyramid.get_max_blocks(0) == 0)
    assert(pyramid.get_max_blocks(1) == 1)
    assert(pyramid.get_max_blocks(2) == 3)
    assert(pyramid.get_max_blocks(3) == 6)
    assert(pyramid.get_max_blocks(4) == 10)
    assert(pyramid.get_max_blocks(5) == 15)
    assert(pyramid.get_max_blocks(6) == 21)

    print("Evaluate get_min_blocks function")
    assert(pyramid.get_min_blocks(0) == 0)
    assert(pyramid.get_min_blocks(1) == 1)
    assert(pyramid.get_min_blocks(2) == 3)
    assert(pyramid.get_min_blocks(3) == 6)
    assert(pyramid.get_min_blocks(4) == 10)
    assert(pyramid.get_min_blocks(5) == 15)
    assert(pyramid.get_min_blocks(6) == 21)

if __name__ == '__main__':
    main()
