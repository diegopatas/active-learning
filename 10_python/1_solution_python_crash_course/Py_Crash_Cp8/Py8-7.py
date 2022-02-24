# Program that describes a musci album
def make_album(artist: str, album: str, rec: int = None):
    """Describes an album."""
    reg = {'art': artist, 'alb': album}
    if rec:
        reg['faixa'] = rec
    return reg

alb21 = make_album('adele', '21', 13)
albimagine = make_album('beatles', 'strawberry')
albtri = make_album('tribalistas', 'encontro')
print(f"{alb21}\n{albimagine}\n{albtri}")
