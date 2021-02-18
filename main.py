import textwrap
import random
import os

import sys

id = 0
PATH = "data/"


def append_file_to_file(file1, file2_name):
    file1.writelines(open(file2_name, "r").readlines())


def write_to_latex(list_9_songs, name=None):
    global id
    id += 1
    if not name:
        file = open(f"{PATH}/kaart{id}.tex", "w+")
    else:
        file = open(f"{PATH}/kaart_{name}.tex", "w+")
    append_file_to_file(file, "pre.tex")
    for i, s in enumerate(list_9_songs):
        file.write(
            "\parbox{3cm}{\centering \\textbf{"+s + "}}")
        if i % 4 == 3:
            file.write(f"\\\\ \\\\ \n")
        else:
            file.write("& \n")

    append_file_to_file(file, "post.tex")

    file.close()


def get_latex_files(p):
    return [i for i in os.listdir(p) if i.endswith(".tex")]


def all_latex_to_pdf():
    files = get_latex_files(PATH)
    [os.system(f"pdflatex -output-directory {PATH} {PATH}/{file} ")
     for file in files]

    print(files)


def read_from_file(file="songs.txt"):
    f = open(file, "r")
    return [i.strip() for i in f.readlines()]


def get_rows(l):
    size = int(len(l)**0.5)
    r = [[]] * size
    for i in range(size):
        for j in range(size):
            r[i].append(l[j*size + i])
    return [set(a) for a in r]


def get_cols(l):

    size = int(len(l)**0.5)
    r = [[]] * size
    for i in range(size):
        for j in range(size):
            r[i].append(l[i*size + j])
    return [set(a) for a in r]


def get_diagonal(l):
    r = [[], []]
    size = int(len(l)**0.5)
    for i in range(size):
        r[0].append(l[i*size + i])
        r[1].append(l[(i+1)*size - i])
    return [set(a) for a in r]


def get_all_bingo_posibilities(l) -> set:
    return get_rows(l) + (get_cols(l)) + (get_diagonal(l))


def check_if_same_bingo(list_a, list_b) -> bool:
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


def create_n_random_cards(list_songs, n=50):
    list_list_songs = []
    gen = perm_generator(list_songs)
    for i in range(n):
        list_list_songs.append(next(gen)[: 16])

    return list_list_songs


def main():

    songs = read_from_file()
    print(f"Read {len(songs)} song{'s' if len(songs) != 1 else ''} from file")

    if len(sys.argv) >= 2:
        card = create_n_random_cards(songs, 1)[0]
        write_to_latex(card, sys.argv[1])
        os.system(
            f"pdflatex -output-directory {PATH} {PATH}/kaart_{sys.argv[1]}.tex")

    else:
        list_list_songs = create_n_random_cards(songs, 600)

        for card in list_list_songs:
            write_to_latex(card)

        all_latex_to_pdf()


if __name__ == "__main__":
    main()
