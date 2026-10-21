from pyscript import display, document

def fullname(e):
    document.getElementById('output').innerHTML = ' '
    first_name = document.getElementById('firstname').value
    last_name = document.getElementById('lastname').value

    full_name = first_name + last_name

    grade7 = {'Mikasa Ackerman', 'Eren Yeager', 'Armin Arlert', 'Hange Zoe', 'Levi Ackerman'}
    grade7.add(first_name + last_name)
    display(grade7, target='output') 

    display_message =(f'Total number of members = : 6')
    display(display_message, target='output')
    

    
    # display(full_name | grade7, target='output') #counting the items




