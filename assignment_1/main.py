
def check_name():
    name_string = 'Trey Schneider'
    if name_string.find('Schneider') != -1:
        print('found')
    else:
        print('not found')

check_name()

def check_user_name(username):
    return username.isalnum()

# print(check_user_name('wow123/'))

