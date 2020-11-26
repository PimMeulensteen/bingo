import textwrap
import random
id = 0


def write_to_latex(list_9_songs):
    global id
    id += 1
    file = open(f"data/kaart{id}.tex", "w+")
    pre_latex = open("pre.tex", "r")
    file.writelines(pre_latex.readlines())

    for i, s in enumerate(list_9_songs):
        file.write(
            "\parbox{3cm}{\centering \\textbf{"+s + "}}")
        if i % 4 == 3:
            file.write(f"\\\\ \\\\ \n")
        else:
            file.write("& \n")

    post_latex = open("post.tex", "r")
    file.writelines(post_latex.readlines())

    file.close()


def read_from_file(file="songs.txt"):
    f = open(file, "r")
    return [i.strip() for i in f.readlines()]


def perm_generator(seq):
    seen = set()
    length = len(seq)
    while True:
        perm = tuple(random.sample(seq, length))
        if perm not in seen:
            seen.add(perm)
            yield perm


def create_n_random_cards(list_songs, n=50):
    list_list_songs = []
    gen = perm_generator(list_songs)
    for i in range(n):
        list_list_songs.append(next(gen)[:16])

    return list_list_songs


def main():
    songs = read_from_file()
    print(f"Read {len(songs)} song{'s' if len(songs) != 1 else ''} from file")

    list_list_songs = create_n_random_cards(songs)

    for card in list_list_songs:
        write_to_latex(card)


if __name__ == "__main__":
    main()
