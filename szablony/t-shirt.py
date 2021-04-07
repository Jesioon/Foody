sandwich_orders = ['z szynką', 'z serem', 'wege', 'mięsną', 'z ogórkiem']
finished_sandwiches = []

for sandwich in sandwich_orders:
    sandwich_orders.remove(sandwich)
    print(sandwich)
    print(sandwich_orders)