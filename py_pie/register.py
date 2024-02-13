import cgi
import cgitb

print('Content-Type: text/html')
print()

cgitb.enable()

form = cgi.FieldStorage()

username = form.getvalue('username')
gender = form.getvalue("gender")
course = form.getvalue('course')
mobile = form.getvalue("mobile")

print('')
print('')
print('''
    Data received from Client browser with POST method
''')
print('Name: {}'.format(username))
print('Gender: {}'.format(gender))
print('Course: {}'.format(course))
print('Mobile: {}'.format(mobile))
print('')
print('')
