import tool
def logging(id,lines,source):
    nana=open(tool.path("log",id)+source,"a")
    nana.write(lines+"\n")
    nana.close()
    print(lines)

#def logset(id,sets,location):    lines=""    for n in range(0,len(sets)):        lines=lines+sets[n]        if n == len(sets):            lines=lines+"\n"        else:            lines=lines+","    logging(id,lines,location)
