def rle(string):
    i=0
    resultsring=""
    while i<len(string):
        count=1
        while i+1<len(string) and  string[i]==string[i+1]:
            count+=1
            i+=1
        if count==1:
            resultsring+=string[i]
        else:
            resultsring+=string[i]+str(count)
        i+=1
    return resultsring

s=input()
if s<"Z" and s>"A":
    print(rle(s))
else:
    print("ERROR")               