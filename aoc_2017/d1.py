"""
The captcha requires you to review a sequence of digits (your puzzle input) and find the sum of all
digits that match the next digit in the list. The list is circular, so the digit after the last digit
is the first digit in the list.

For example:

1122 produces a sum of 3 (1 + 2) because the first digit (1) matches the second digit and the third digit (2) matches the fourth digit.
1111 produces 4 because each digit (all 1) matches the next.
1234 produces 0 because no digit matches the next.
91212129 produces 9 because the only digit that matches the next one is the last digit, 9.
"""

d1 = '649713959682898259577777982349515784822684939966191359164369933435366431847754488661965363557985166219358714739318371382388296151195361571216131925158492441461844687324923315381358331571577613789649166486152237945917987977793891739865149734755993241361886336926538482271124755359572791451335842534893192693558659991171983849285489139421425933638614884415896938914992732492192458636484523228244532331587584779552788544667253577324649915274115924611758345676183443982992733966373498385685965768929241477983727921279826727976872556315428434799161759734932659829934562339385328119656823483954856427365892627728163524721467938449943358192632262354854593635831559352247443975945144163183563723562891357859367964126289445982135523535923113589316417623483631637569291941782992213889513714525342468563349385271884221685549996534333765731243895662624829924982971685443825366827923589435254514211489649482374876434549682785459698885521673258939413255158196525696236457911447599947449665542554251486847388823576937167237476556782133227279324526834946534444718161524129285919477959937684728882592779941734186144138883994322742484853925383518651687147246943421311287324867663698432546619583638976637733345251834869985746385371617743498627111441933546356934671639545342515392536574744795732243617113574641284231928489312683617154536648219244996491745718658151648246791826466973654765284263928884137863647623237345882469142933142637583644258427416972595241737254449718531724176538648369253796688931245191382956961544775856872281317743828552629843551844927913147518377362266554334386721313244223233396453291224932499277961525785755863852487141946626663835195286762947172384186667439516367219391823774338692151926472717373235612911848773387771244144969149482477519437822863422662157461968444281972353149695515494992537927492111388193837553844671719291482442337761321272333982924289323437277224565149928416255435841327756139118119744528993269157174414264387573331116323982614862952264597611885999285995516357519648695594299657387614793341626318866519144574571816535351149394735916975448425618171572917195165594323552199346814729617189679698944337146'

t1 = '1122'
t2 = '1111'
t3 = '1234'
t4 = '91212129'

t5 = '1212'
t6 = '1221'
t7 = '123425'
t8 = '123123'
t9 = '12131415'


def get_sum(ds, species='type1'):
    sums = 0
    l = len(ds)
    if species == 'type1':
        offset = 1
    elif species == 'type2':
        offset = int(l/2)
    return sum((int(e) for idx, e in enumerate(ds) if e == ds[(idx + offset) % l]))


"""
Now, instead of considering the next digit, it wants you to consider the digit halfway around the circular list. That is, if your list contains 10 items, only include a digit in your sum if the digit 10/2 = 5 steps forward matches it. Fortunately, your list has an even number of elements.

For example:

1212 produces 6: the list contains 4 items, and all four digits match the digit 2 items ahead.
1221 produces 0, because every comparison is between a 1 and a 2.
123425 produces 4, because both 2s match each other, but no other digit has a match.
123123 produces 12.
12131415 produces 4.
"""

if __name__ == '__main__':
    DEBUG = False
    tests = [t1, t2, t3, t4]
    if DEBUG:
        for t in tests:
            print(f'\nSum : {get_sum(t)}')
    else:
        print(f'\nPart I Sum : {get_sum(d1)}')
    tests = [t5, t6, t7, t8, t9]
    if DEBUG:
        for t in tests:
            print(f'\nSum : {get_sum(t, species="type2")}')
    else:
        print(f'\nPart II Sum : {get_sum(d1, species="type2")}')

"""
import re
def solve_regex(captcha, n):
    return sum(int(c) for c in re.findall(fr'(\d)(?=.{{{n-1}}}\1)', captcha+captcha[:n]))

solve_regex(captcha, 1)
solve_regex(captcha, len(captcha) // 2)
Things used (you can read about Python's regular expression syntax here):
re.findall function.
(\d) matches a digit and then its twin with \1.
(?=.{n-1}\1) matches any n-1 symbols between the previous digit and the twin, but doesn’t consume the string. This way we check every digit and don't skip any.
PEP 498 -- Literal String Interpolation. It makes us use triple braces, the inner pair for interpolation and two outer pairs (you need to escape braces in f-strings) which boil down to a pair in the final regex string. So if n is 1, we end up with (\d)(?=.{0}\1) which matches two successive identical digits. Somebody may prefer %-format like r'(\d)(?=.{%d}\1)' % n-1, but I like f-strings more.
This solution doesn't support n greater than len(captcha). In that case you'd better use manual iteration with (i+n) % len(captcha) on each step. It also doesn't work for infinite streams of characters.
"""