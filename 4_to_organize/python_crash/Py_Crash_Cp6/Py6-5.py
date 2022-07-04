# Program of a dictionary of rivers
rivers = {
    'tiete': 'sao paulo',
    'pinheiros': 'sao paulo',
    'nilo': 'egito',
    'sao_francisco': 'pernambuco',
}
for k, v in rivers.items():
    print(f"The {k.title()} runs through {v.title()}.")

for k in rivers.keys():
    print(k)
for v in set(rivers.values()):
    print(v)
