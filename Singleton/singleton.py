from tigger import Tigger
# It may not get imported if we import all modules using *

a = Tigger()
b = Tigger()

print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Are they the same object? {a is b}')