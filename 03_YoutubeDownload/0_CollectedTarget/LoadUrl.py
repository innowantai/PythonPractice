





def LoadAllUrl(fileName):
    fp = open(fileName,"+r")
    line = fp.readline()
    AllUrl = [];
    while line:
        AllUrl.append(line);
        line = fp.readline();
        #print(line)    
    fp.close;
    print("Loadind Completed : All_Url done!")
    return AllUrl





