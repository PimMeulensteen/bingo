from typing import Callable, List, TextIO, Union, Tuple
import random
import os

import sys
random.seed(0, 1)

id = 0
PATH = "data/"  # saving files in this folder
SIZE = 5  # make the grid SIZE x SIZE.

PRE_ITEM = r"\fbox{\parbox[][4.5cm][c]{4.5cm}{\centering \large\textbf{"
POST_ITEM = "}}}"

CardItem = str


def append_file_to_file(file1: TextIO, file2_name: str) -> None:
    """ Open file1 and add the contents of the file with then name file2 to
    it. """
    file1.writelines(open(file2_name, "r").readlines())


def write_to_latex(list_9_songs: List[CardItem], name=None) -> None:
    global id
    id += 1

    if not name:
        file = open(f"{PATH}/kaart{id}.tex", "w+")
    else:
        file = open(f"{PATH}/kaart_{name}.tex", "w+")

    append_file_to_file(file, "pre.tex")

    for i, carditem in enumerate(list_9_songs):
        file.write(PRE_ITEM + carditem + POST_ITEM)
        if i % SIZE == (SIZE-1):
            file.write("\\\\ \\\\ \n")
        else:
            file.write("& \n")

    append_file_to_file(file, "post.tex")

    file.close()


def get_file_type(dir: str, type: str) -> List[str]:
    return [i for i in os.listdir(dir) if i.endswith("." + type)]


def all_latex_to_pdf():
    files = get_file_type(PATH, "tex")
    [os.system(f"pdflatex -output-directory {PATH} {PATH}/{file} ")
     for file in files]

    pdfs = get_file_type(PATH, "pdf")
    pdfs_raw = [i for i in pdfs if not i.startswith("persco_")]
    [os.system(f"pdftk {PATH}/{file} cat 1 output {PATH}/persco_{file}  ")
     for file in pdfs_raw]


def read_from_file(file: str = "songs.txt") -> List[CardItem]:
    f = open(file, "r")
    return [i.strip() for i in f.readlines()]


def get_rows(l: List[CardItem]):
    r = [[]] * SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            r[i].append(l[j*SIZE + i])
    return [set(a) for a in r]


def get_cols(l: List[CardItem]):
    r = [[]] * SIZE
    for i in range(SIZE):
        for j in range(SIZE):
            r[i].append(l[i*SIZE + j])
    return [set(a) for a in r]


def get_diagonal(l: List[CardItem]):
    r = [[], []]
    for i in range(SIZE):
        r[0].append(l[i*SIZE + i])
        r[1].append(l[(i+1)*SIZE - i])
    return [set(a) for a in r]


def get_all_bingo_posibilities(l: List[CardItem]) -> set:
    return get_rows(l) + (get_cols(l)) + (get_diagonal(l))


def check_if_same_bingo(list_a: List[CardItem], list_b: List[CardItem]) -> bool:
    return bool(get_all_bingo_posibilities(list_a).union(get_all_bingo_posibilities(list_b)))


def perm_generator(seq):
    seen = set()
    bingo_seen = []
    length = len(seq)
    while True:
        perm = tuple(random.sample(seq, length))
        if perm not in seen and not any([a in bingo_seen for a in get_all_bingo_posibilities(perm)]):
            seen.add(perm)
            bingo_seen += list(get_all_bingo_posibilities(perm))
            yield perm


def create_n_random_cards(list_songs: List[CardItem], n=50) -> List[List[CardItem]]:
    list_list_songs = []
    gen = perm_generator(list_songs)
    for i in range(n):
        list_list_songs.append(next(gen)[: SIZE**2])

    return list_list_songs


def main():
    songs = read_from_file()
    print(f"Read {len(songs)} word{'s' if len(songs) != 1 else ''} from file")

    if len(sys.argv) >= 2:
        card = create_n_random_cards(songs, 1)[0]
        write_to_latex(card, sys.argv[1])
        os.system(
            f"pdflatex -output-directory {PATH} {PATH}/kaart_{sys.argv[1]}.tex"
        )

    else:
        list_list_songs = create_n_random_cards(songs, 50)
        for card in list_list_songs:
            write_to_latex(card)

        all_latex_to_pdf()



if __name__ == "__main__":
    main()
