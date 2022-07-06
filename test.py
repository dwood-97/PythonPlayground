string1 = []
sub_string1 = []

def count_substring(string, sub_string):
    return


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)
    
    for chr in range(0, len(string)):
        string1.append(ord(string[chr]))

#print(string1)

    for chr in range(0, len(sub_string)):
        sub_string1.append(ord(sub_string[chr]))
    #print(string1)
    
if int(sub_string1) == int(string1):
    print(sub_string1)