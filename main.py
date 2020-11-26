
def write_to_latex(list_9_songs):
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

    list_list_songs = create_n_random_cards(songs)
    for card in list_list_songs:
        write_to_latex(card)


if __name__ == "__main__":
    main()
