def split_n_strip(str):

    t = str.split()

    # t[0] will now be the range. split with '-'
    # t[1] will be the character. strip ':'
    # leave t[2] unmodified
    return [t[0].split('-'), t[1].strip(':'), t[2]]