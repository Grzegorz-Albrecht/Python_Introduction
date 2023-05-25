num_rows=int(input())
num_columns=int(input())
def print_operatprint_operation_table(operation, num_rows, num_columns):
    for x in range (1,num_rows+1):
        for y in range (1,num_columns+1):
            print(*list(map(operation,[x],[y])),end=(' '))
        print()

operation=lambda x,y:x*y
print_operatprint_operation_table(operation,num_rows,num_columns)    