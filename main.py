
#profe, por si no me reviso la primera tarea, o esta tarea en kodland, no puedo ingresar al grupo con el link que esta en kodland

slangs_dict = {
    'cringe': 'algo embarazoso o extraño',
    'lol': 'abreviacion, significa "riendose fuertemente"',
    'looksmaxxing': 'grupo de ejercicios los cuales supuestamente mejoran la forma de la cara'
}

word = input('Cual palabra actual no conoces? :')

if word in slangs_dict:
    print(word, slangs_dict[word] )
else:
    print('no tengo esa definicion')
