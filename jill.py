import hashlib
import argparse
# h = file containing passwords
# d = pasword dictionary 
#python3 jill.py passwords.txt wordlist.txt -v -a sha512
#username:sha256(password)

def pacrack(d, h):
    F = open(h, 'r')
    D = open(d, 'r')
    Flines = F.readlines()
    Dlines = D.readlines()
    A = []
    B =[]
    C = []
    Ko = []

    def hash(password):
        sha256_hash = hashlib.sha256()
        sha256_hash.update(password.encode('utf-8'))
        return sha256_hash.hexdigest()
    #turns input into hash

    for E in Flines:
        Flines[Flines.index(E)] = E.strip() #strips new line characters
    for E in Flines:
        A.append(f"{hash(E)}")
        #change E(potential passwords) - strip E of new line character - then put E into A as a hashed passowrds

    for L in Dlines:
        Dlines[Dlines.index(L)] = L.strip() #strips new line characters
    for i in Dlines: 
        g = i.split(":") #splits usernames from passwords
        for r in g:
            if g.index(r) == 0:
                #adds names to list C
                C.append(r)
            elif g.index(r) == 1:
                #adds hashed passwords to list B
                B.append(r)
        #strip L(usernames and passwords(hashed)) then put password into list B and puts usernames into list C
    

    for i in B:
        for t in A:
            if i == t:
                Ko.append(C[B.index(i)]+":"+Flines[A.index(t)]) #glues usernames backtogether with found passwords
        #compares hashed passwords from list B with list A   

    F.close()
    D.close()
    return Ko #returns founds passwords

def main(): #allows to be used in command line
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('filename2')
    args = parser.parse_args()
    count = pacrack(args.filename, args.filename2)
    for x in count:
        print(x)

if __name__ == '__main__':
    main()