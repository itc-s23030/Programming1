def concat_words(*args, separator="."):
    print(separator.join(args))


concat_words("a", "b", "c", "d", separator="_")
concat_words("4_choume", "Minatoku", "Tokyo", "Japan", separator=" ")
