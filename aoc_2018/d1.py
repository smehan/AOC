"""
Current frequency  0, change of +1; resulting frequency  1.
Current frequency  1, change of -2; resulting frequency -1.
Current frequency -1, change of +3; resulting frequency  2.
Current frequency  2, change of +1; resulting frequency  3.
In this example, the resulting frequency is 3.

Here are other example situations:

+1, +1, +1 results in  3
+1, +1, -2 results in  0
-1, -2, -3 results in -6

"""


def prepare(s: str) -> list:
    s.replace("+", "")
    out = []
    for e in s.split(","):
        out.append(int(e))
    return out


def cur_freq(freqs: list) -> int:
    out = 0
    for e in freqs:
        out += e
    return out


if __name__ == '__main__':
    assert prepare("+1, -2, +3, +1") == [1, -2, 3, 1]
    assert cur_freq(prepare("+1, -2, +3, +1")) == 3
    assert cur_freq(prepare("+1, +1, +1")) == 3
    assert cur_freq(prepare("+1, +1, -2")) == 0
    assert cur_freq(prepare("-1, -2, -3")) == -6

