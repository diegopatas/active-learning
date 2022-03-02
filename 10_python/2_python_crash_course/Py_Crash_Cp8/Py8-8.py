# Program ALBUM LOOP
def make_album(art: str, alb: str):
    """Creates a album dictionary"""
    muscinfo = {'artist': art, 'album': alb}
    return muscinfo

active = True
while active:
    artinfo = input(f"Enter the artist's name (type 'q' to exit): ")
    albinfo = input(f"Enter the artist's album (type 'q' to exit): ")

    if artinfo == 'q' or albinfo == 'q':
        active = False
    else:
        piece = make_album(artinfo, albinfo)
        print(piece)