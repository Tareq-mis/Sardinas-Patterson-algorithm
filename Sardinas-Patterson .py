"""
Sardinas-Patterson test for unique decodability. A code is not uniquely decodable
if and only if there exists a finite sequence of code symbols which
can be resolved into sequences of code words in two different ways.
Let
g : X ! Y
be a code by characters (letters). Thusd g(xi) = Ki is a code word for xi
(Ki 6= ;): Let K be the set of code words. The code words are assumed to
be distinct. We say that the sequence A is a prefix of the sequence B if B
may be written as AC for some sequence C:
We now present a testing procedure that can always be used to determine
whether or not a code is uniquely decipherable. To see how the procedure
works considet the examples.
We construct a sequence of sets Sm; m = 0; 1; 2; : : : ; as follows. Let S0 = K
be the original set of code words. To form S1; we look at all pairs of code
words in S0: If a code word Ki; is a prefix of another code word Kj that
is, Kj = KiA; we place the suffix A in S0: In general, to form Sn; n > 1,
we compare S0 and Sn􀀀1: If a code word Ki 2 S0 is a prefix of a sequence
A = KiB 2 Sn􀀀1; the suffix B is placed in Sn and if a sequence A0 2 Sn􀀀1 is
a prefix of a code word Ki = A0B0 2 S0; we place the suffix B0 2 Sn:
"""

def RemovingprefixOfWord(setofprefixs, w):
    """removing any prefix in setofprefixs."""
    for p in setofprefixs:
        if w.startswith(p):
            yield w[len(p):]
    return

def CodeWordprefix(setofprefixs, ws):
    """Returns the set of suffixes of any word in ws after removing any prefix
    in setofprefixs."""
    setofsuffixes = set()
    for w in ws:
        for q in RemovingprefixOfWord(setofprefixs, w):
            if q != '':
                setofsuffixes.add(q)
            #print(q)
    if setofsuffixes :
        print("setofsuffixes = ", str(setofsuffixes))

    return setofsuffixes
def IsTheCodeUniquelyDeciperable(cs):
    """Checks if the set of codewords cs is uniquely decodable via the
    Sardinas-Patterson algorithm."""
    NL, i = len(str(cs)) * len(str(max(len(x) for x in cs))), 1
    s = CodeWordprefix(cs, cs)
    s.discard('')
    if len(s) == 0:
        print('Uniquely Deciperable pre code.')
        return True
    while '' not in s and len(s & cs) == 0:
        t = CodeWordprefix(cs, s) | CodeWordprefix(s, cs)
        if t == s or i > NL + 1:
            print('Uniquely decodable.')
            return True
        s = t
        i += 1
    if '' in s:
        print('Dangling empty suffix.')
    for x in s & cs:
        print('The code is not uniquely decipherable because it has Dangling suffix: {}'.format(x))
    return False

if __name__ == '__main__':

    SetOfCodewords = {'xyx', 'xxxy', 'xyyx', 'yyxx', 'xxxyy', 'xxyyx', 'yyyyx', 'yxyxyy'}
    print('The Set of Codewords',SetOfCodewords)
    IsTheCodeUniquelyDeciperable(SetOfCodewords)
