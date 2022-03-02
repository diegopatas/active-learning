# Programa lista de convidados
lis_conv = ['maju', 'cesar', 'bocardi']
print(f"Hello {lis_conv[0]. title()} I would like to invite you to my dinner party.\n"
      f"Hello {lis_conv[1]. title()} I would like to invite you to my dinner party.\n"
      f"Hello {lis_conv[2]. title()} I would like to invite you to my dinner party.")
print(f"Dinner party updates:\n"
      f"Hi everyone, I would like to informe that {lis_conv[2].title()} won't join us tonight! Sorry.")
lis_conv.remove('bocardi')
print(f"\nThe actual list of people invited is:")
print(lis_conv[0].title(), lis_conv[1].title())
lis_conv.append('kerman')
print(f'\nThe new guest is {lis_conv[2].title()}.')
print(f"\nHi guys, I've just found a new, bigger table, so I decided to invite more people to the dinner party.")
lis_conv.append('lais')
lis_conv.append('jeferson')
print(f"\nThe actual guests are:\n"
      f"{lis_conv[0].title()}\n{lis_conv[1].title()}\n{lis_conv[2].title()}\n{lis_conv[3].title()}\n{lis_conv[4].title()}")