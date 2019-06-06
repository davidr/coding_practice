input_num = (
    "73167176531330624919225119674426574742355349194934"
    "96983520312774506326239578318016984801869478851843"
    "85861560789112949495459501737958331952853208805511"
    "12540698747158523863050715693290963295227443043557"
    "66896648950445244523161731856403098711121722383113"
    "62229893423380308135336276614282806444486645238749"
    "30358907296290491560440772390713810515859307960866"
    "70172427121883998797908792274921901699720888093776"
    "65727333001053367881220235421809751254540594752243"
    "52584907711670556013604839586446706324415722155397"
    "53697817977846174064955149290862569321978468622482"
    "83972241375657056057490261407972968652414535100474"
    "82166370484403199890008895243450658541227588666881"
    "16427171479924442928230863465674813919123162824586"
    "17866458359124566529476545682848912883142607690042"
    "24219022671055626321111109370544217506941658960408"
    "07198403850962455444362981230987879927244284909188"
    "84580156166097919133875499200524063689912560717606"
    "05886116467109405077541002256983155200055935729725"
    "71636269561882670428252483600823257530420752963450"
)


def compute(adjacent_digits: int = 4) -> int:
    # okay, the trick they want here is obviously to avoid doing adjacent_digits multiplies for every
    # time we move the window of digits to multiply. I think the best thing to do is to divide the
    # oldest digit out and multiply the newest one in.
    #
    # [time passes]
    #
    # although after I implemented the 0 value skipping, it brought it down to only 263 possible 13-digit
    # sequences to multiply out, which doesn't really need any more optimizing
    #
    # I think I overthought this

    window_start_idx = -1
    highest_product = -1

    while window_start_idx + adjacent_digits <= len(input_num) - 1:
        # Since we break out given various criteria, it makes sense to just increment the index counter
        # before we start working
        window_start_idx += 1

        # easier indexing:
        i = window_start_idx
        j = window_start_idx + adjacent_digits

        if '0' in input_num[i:j]:
            continue

        current_product = 1
        for k in input_num[i:j]:
            current_product *= int(k)

        if current_product > highest_product:
            highest_product = current_product

    return highest_product
