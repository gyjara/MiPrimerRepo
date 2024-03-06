color=  'Pink'
match color:
    case 'Red':
        print("Es rojo")
    case 'Blu':
        print("Es Azul")
    case 'Green':
        print("Es Verde")
    case _:
        print('Ese color no está aqui')


mes='1'
match mes:
    case '1':
        print("January")
    case '2':
        print("Febrery")
    case '3':
          print("March")
    case '4':
        print("Abril")
    case '5':  
        print("May")
    case '6':
        print("June")
    case '7':
          print("July")
    case '8':
        print("Augots")
    case '9':
        print("Setember")
    case '10':
          print("October")
    case '11':
        print("Nobember")
    case '10':
        print("Desember")
    case _:
        print("El mes no existe")