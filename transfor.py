import  os

stro = input("Please input a directory to upload\n:")
if(os.path.exists(stro)):
    for root, dirs, files in os.walk(stro, topdown=False):
        dirrr=[]

        for name in files:

            dirrr = name.split('.')
            if dirrr[-1] == 'txt':
                print(dirrr)
                print(os.path.join(root, name))
                fo = open(os.path.join(root,name),'r+')
                a = fo.readline().replace('\n','')
                b = fo.readline().replace('\n','')
                ele = a.rsplit('\t')
                print(ele)
                num = b.rsplit('\t')
                print(num)
                restr = ''
                for nn in range(0,len(ele)):
                    if num[nn] != '0':
                        nm = num[nn]
                        nc = str(nm)
                        restr += ele[nn]+':'+ nc +','
                readwrit = restr[:len(restr)-1]
                print(readwrit)
                fo.write(readwrit)
                fo.close()



