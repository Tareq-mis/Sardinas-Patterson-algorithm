# Sardinas-Patterson-algorithm

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
