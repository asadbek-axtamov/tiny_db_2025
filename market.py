from tinydb import TinyDB
db = TinyDB('market.json')

products = [
    {'name': 'Galaxy Watch Ultra', 'cost': 350, 'color': 'titan'},
    {'name': 'Galaxy S25 Ultra', 'price': 1300, 'color': 'black', 'memory': 512},
    {'name': 'Galaxy Book5 Pro', 'price': 1100, 'color': 'gold', 'memory': 1024}
]

db.insert_multiple(products)