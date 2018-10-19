def checkletter(ltr):
    dit = 0
    new = (global new)
    
    print(new)
    input()
    
    global strike
    newbefore = new

    for chk in word:
    
        if chk == ltr:
            displist[dit] = ltr
            new = new+1
        dit = dit+1

    if new != newbefore:

        dispstr = ""

        for rpl in displist:
            dispstr = dispstr+rpl
        
    else:
        strike = strike+1