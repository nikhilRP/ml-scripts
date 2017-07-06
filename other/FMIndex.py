# This script was written mostly for my understanding of text indices
EOS = "\0"


class FMIndex(object):
    def __init__(self, data):
        self.data = bwt(data)
        self.offset = {}
        self._build(data)

    def _build(self, data):
        """ build the index """
        self.occ = first_occ(self.data)

    def _occ(self, qc):
        c = self.occ.get(qc)
        if c is None:
            return 0
        return c

    def _count(self, idx, qc):
        """count the occurances of letter qc (rank of qc) upto position idx """
        if qc not in self.occ.keys():
            return 0
        c = 0
        for i in xrange(idx):
            if self.data[i] == qc:
                c += 1
        return c

    def _lf(self, idx, qc):
        """ get the nearset lf mapping for letter qc at position idx """
        o = self._occ(qc)
        c = self._count(idx, qc)
        return o + c

    def _walk(self, idx):
        """ find the offset in position idx of transformed string
            from the beginning """
        r = 0
        i = idx
        while self.data[i] != EOS:
            if self.offset.get(i):
                r += self.offset[i]
                break
            r += 1
            i = self._lf(i, self.data[i])
        if not self.offset.get(idx):
            self.offset[i] = r
        return r

    def bounds(self, q):
        """ find the first and last suffix positions for query q """
        top = 0
        bot = len(self.data)
        for i, qc in enumerate(q[::-1]):
            top = self._lf(top, qc)
            bot = self._lf(bot, qc)
            if top == bot:
                return (-1, -1)
        return (top, bot)

    def search(self, q):
        """ search the positions of query q """

        # find the suffixes for the query
        top, bot = self.bounds(q)
        matches = []
        # find the location of the suffixes
        # by walking the reverse text from that position
        # with lf mapping
        for i in range(top, bot):
            pos = self._walk(i)
            matches.append(pos)
        return sorted(matches)

    def count(self, q):
        """ count occurances of q in the index """
        top, bot = self.bounds(q)
        return bot - top

    def getOriginal(self):
        return ibwt(self.data)

    def RLE(self):
        output = []
        last = ''
        k = 0
        for i in range(len(self.data)):
            ch = self.data[i]
            if ch == last:
                k += 1
            else:
                if k > 0:
                    output.append((last, k))
                last = ch
                k = 1
        output.append((last, k))
        return output


def bwt(s):
    """Apply Burrows-Wheeler transform to input string."""
    assert "\0" not in s, "Input string cannot contain null character ('\\0')"
    s += "\0"  # Add end of file marker
    table = sorted(s[i:] + s[:i] for i in range(len(s)))
    last_column = [row[-1:] for row in table]
    return "".join(last_column)


def ibwt(r):
    """Convert bwt index back to string."""
    table = [""] * len(r)
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))
    s = [row for row in table if row.endswith("\0")][0]
    return s.rstrip("\0")


def first_occ(s):
    A = {}
    for i, c in enumerate(s):
        if A.get(c):
            A[c] += 1
        else:
            A[c] = 1
    letters = sorted(A.keys())
    occ = {}
    idx = 0
    for c in letters:
        occ[c] = idx
        idx += A[c]
    del idx, A
    return occ


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Print BWT and FM-index of a given DNA sequence",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument('--read-seq', help="Sequence")
    args = parser.parse_args()
    print "Input - " + args.read_seq
    fm_index = FMIndex(args.read_seq)
    print(fm_index)


if __name__ == '__main__':
    main()
