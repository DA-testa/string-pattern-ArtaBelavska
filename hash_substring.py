# python3

def read_input():
    darbiba =input("Enter I or F: ")
    if "I" in darbiba:
        pattern=input().strip()
        text =input().strip()

    elif "F" in darbiba:
        fileName='./tests/06'
        try:
            with open(fileName, 'r') as f:
                pattern=f.readline().strip()
                text=f.readline().strip()
        except Exception as j:
            print("Error:", str(j))
            return
    else:
        print("Error: invalid darbiba")
        return
    return pattern,text
   
def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # this function should find the occurances using Rabin Karp alghoritm
    garumsPattern=len(pattern)
    garumsText=len(text)
    hashPattern=hash(pattern)
    hashText= hash(text[:garumsPattern])
    # and return an iterable variable
    gadijumi=[]
    for i in range(garumsText-garumsPattern + 1):
       # hashText= hash(text[i:i + garumsPattern])
        
        if hashText==hashPattern and pattern==text[i:i + garumsPattern]:
            gadijumi.append(i)
        if (i < garumsText-garumsPattern):
            hashText=hash(text[i + 1: i + garumsPattern + 1])
    return gadijumi


# this part launches the functions
if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

