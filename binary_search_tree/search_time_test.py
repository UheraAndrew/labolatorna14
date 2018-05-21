from random import choice, shuffle
from time import time

from linkedbst import LinkedBST


def linear_search(lst, search_words):
    start_time = time()
    for i in search_words:
        if i in lst:
            pass
    return time() - start_time


def unbalanced_bst_search(bst: LinkedBST, search_words):
    start_time = time()
    for i in search_words:
        bst.find(i)
    return time() - start_time


def balanced_bst_search(bst: LinkedBST, search_words):
    bst.rebalance()
    start_time = time()
    for i in search_words:
        bst.find(i)
    return time() - start_time


def main():
    with open("words.txt", encoding="UTF-8", errors="ignore") as f:
        words = [word.strip() for word in f]

    bst = LinkedBST()
    for item in set(words):
        bst.add(item)

    test_words = []
    for i in range(10 ** 4):
        test_words.append(choice(words))

    print("Start test")
    print(f"linear_search time = "
          f"{linear_search(words,test_words)}")
    print(f"unbalanced_bst_search time = "
          f"{unbalanced_bst_search(bst,test_words)}")
    print(f"balanced_bst_search time = "
          f"{balanced_bst_search(bst,test_words)}")


if __name__ == '__main__':
    main()
