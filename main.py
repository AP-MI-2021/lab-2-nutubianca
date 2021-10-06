def is_palindrome(n):
    ''''
    -determina daca numarul dat este palindrom sau nu
    Input:
    -paramtru: n (de tip int)
    Output:
    -va returna True, daca n este palindrom, sau False, in caz contrar(de tip bool)
    '''
    copie=n
    invers=0
    while copie:
        invers=invers*10+copie%10
        copie=copie//10
    if invers == n:
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(1221) == True
    assert is_palindrome(3453) == False
    assert is_palindrome(565) == True
    assert is_palindrome(717) == True
    assert is_palindrome(9807) == False
    assert is_palindrome(10401) == True
    assert is_palindrome(1232) == False


test_is_palindrome()


def verificare_prim(n):
    if n == 1:
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, n // 2 + 1, 2):
        if n % i == 0:
            return False
    return True


def is_superprime(n):
    ''''
    -deteremina daca un numar este superprim sau nu
    Input:
    -parametru: n (de tip intreg)
    Output:
    -va returna True, daca n este superprim, sau False, in caz contrar(de tip bool)
    '''
    copie = n
    verificare = 1
    #presupunem ca numarul dat este superprim
    while copie:
        if not verificare_prim(copie):
            verificare=0
            break
        copie=copie//10
    if verificare==1:
        return True
    return False


def test_is_superprime():
    assert is_superprime(124) == False
    assert is_superprime(233) == True
    assert is_superprime(1290) == False
    assert is_superprime(239) == True
    assert is_superprime(14) == False


test_is_superprime()


def get_largest_prime_below(n):
    '''
    -determina ultimul numar prim mai mic decat numarul n dat
    Input
    -parametru n(de tip intreg)
    Output
    -nr_prim:ultimul numar prim mai mic decat numarul n dat
    '''
    nr_prim=n-1
    ok=False
    if n<=2:
        return None
    while not ok:
        if verificare_prim(nr_prim):
            ok=True
            break
        nr_prim=nr_prim-1
    return nr_prim


def test_get_largest_prime_below():
    assert get_largest_prime_below(25) == 23
    assert get_largest_prime_below(18) == 17
    assert get_largest_prime_below(36) == 31
    assert get_largest_prime_below(135) == 131
    assert get_largest_prime_below(76) == 73

test_get_largest_prime_below()

def main():
    while True:
        print("1.Determina daca un numar dat este palindrom.")
        print("2.Determina daca un numar dat este superprim.")
        print("3.Determina ultimul numar prim mai mic decat un numar dat.")
        print("x.Iesire")
        optiune=input("Dati optiunea:")
        if optiune=="1":
            numar=int(input("Dati numar:"))
            if is_palindrome(numar):
                print("Numarul dat este palindrom.")
            else:
                print("Numarul dat nu este palindrom.")
        elif optiune=="2":
            numar=int(input("Dati numar:"))
            if is_superprime(numar):
                print("Numarul dat este superprim.")
            else:
                print("Numarul dat nu este superprim.")
        elif optiune=="3":
            numar = int(input("Dati numar:"))
            nrprim=get_largest_prime_below(numar)
            if nrprim:
                print("Ultimul numar prim mai mic decat numarul dat este ",nrprim)
            else:
                print("Nu exista!")
        elif optiune=="x":
            print("Meniul se va inchide.")
            break
        else:
            print("Optiune inexistenta. Reincercati!")


if __name__ == '__main__':
  main()