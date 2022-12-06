def ret(default,clrs,classmain):
    lenclr=len(clrs)
    for x in range(lenclr):
        print("\n")
        print("c-"+classmain+"-"+clrs[x])
        print("{")
        print(default)
        print("color: "+clrs[x])
        print("}")
#default=preexisting css
#clrs=list of colors
#classmain=main color list
