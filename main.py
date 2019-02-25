from display import *
from draw import *
from matrix import *
from random import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
m1 = new_matrix()
m2 = new_matrix()

for i in range(randrange(500)):
    if (randrange(1) == 1):
        add_edge(matrix, randrange(500), randrange(500), randrange(500), randrange(500), randrange(500), randrange(500))
    else:       
        add_point(matrix, randrange(500), randrange(500))


print("Testing add_edge. Adding (1, 2, 3), (4, 5, 6) m2 = \n")
add_edge(m2, 1, 2, 3, 4, 5, 6)
add_edge(m1, 1, 2, 3, 4, 5, 6)
add_edge(m1, 1, 2, 3, 4, 5, 6)
print_matrix(m2)

print("Testing ident. m1 = \n")
ident(m1)
print_matrix(m1)

print("Testing Matrix mult. m1 * m2 = \n")
matrix_mult(m1, m2)
print_matrix(m2)
        
draw_lines( matrix, screen, color )
save_extension(screen,"img.png")
display(screen)

