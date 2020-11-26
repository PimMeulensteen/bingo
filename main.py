import textwrap
id = 0


def write_to_latex(list_9_songs):
    global id
    id += 1
    file = open(f"kaart{id}.tex", "w+")
    file.write(
        r"\documentclass[12pt]{article} \usepackage{eso-pic, graphicx} ")
    file.write("\n")
    file.write(
        r"\usepackage[top=2cm, bottom=2cm, outer=0cm, inner=0cm]{geometry}")
    file.write("\n")
    file.write(
        r"\newcommand{\background}[1]{%")
    file.write("\n")
    file.write(
        r"\AddToShipoutPictureBG*{\includegraphics[width=\paperwidth,height=\paperheight]{#1}}")
    file.write("\n")
    file.write(r"}")

    file.write(r"\begin{document}")
    file.write("\n")
    file.write(
        r" \tabcolsep=30pt \renewcommand{\arraystretch}{4.5}  \topskip0pt \vspace*{4.3cm} \begin{center}  \begin{tabular}{c c c c}")
    file.write("\n")

    for i, s in enumerate(list_9_songs):
        file.write(
            "\parbox{3cm}{\centering "+'\\\\'.join(textwrap.wrap(s, 16)) + "}")
        if i % 4 == 3:
            file.write(f"\\\\ \\\\ \n")
        else:
            file.write("& \n")
    file.write(r"\end{tabular} \background{discobingo.pdf} \end{center}")
    file.write(r" \end{document}")
    file.close()
    raise NotImplementedError


def read_from_file(file="songs.txt"):
    f = open(file, "r")
    return [i.strip() for i in f.readlines()]


def create_n_random_cards(list_songs, n=50):
    raise NotImplementedError

    return list_list_songs


def main():
    songs = read_from_file()
    print(f"Read {len(songs)} song{'s' if len(songs) != 1 else ''} from file")
    # list_list_songs = create_n_random_cards(songs)
    list_list_songs = [songs[:16]]
    for card in list_list_songs:
        write_to_latex(card)


if __name__ == "__main__":
    main()
