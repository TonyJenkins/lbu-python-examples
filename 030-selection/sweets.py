#!/usr/bin/env python3

if __name__ == '__main__':
    
    number_of_friends = int(input('How many friends do you have? '))
    
    if number_of_friends <= 0:
        print('You must have at least one friend!')
    else:
        number_of_sweets = int(input('How many sweets do you have?  '))

        if number_of_sweets < 0:
            print('You cannot have a negative number of sweets!')
        elif number_of_sweets == 0:
            print('You have no sweets to share.How sad.')
        else:
            sweets_each = number_of_sweets // number_of_friends
            left_over = number_of_sweets % number_of_friends

            print(f'With {number_of_friends} friend{"s" if number_of_friends != 1 else ""}, '
                  f'and {number_of_sweets} sweet{"s" if number_of_sweets != 1 else ""}, '
                  f'everyone gets {sweets_each} sweet{"s" if sweets_each != 1 else ""}, '
                  f'and there will be {left_over} left over.')
            
    
