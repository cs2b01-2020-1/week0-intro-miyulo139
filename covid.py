import os
def comparison(files,cuadro):
    def convert_genoma(genoma):
        x = open(genoma, "r")
        x.readline()
        stri = ''
        for linea in x:
            if linea[-1] == '\n':
                linea = linea[:-1]
            stri += str(linea)
        return stri

    for i in range(len(files)):
        for j in range(len(files)):
            count = 0
            gen1=convert_genoma(files[i])
            gen2=convert_genoma(files[j])
            len_comp=min(len(gen1),len(gen2))
            for char_a, char_b in zip(gen1, gen2):
                if char_a == char_b:
                    count+=1
            similitud=round((count*100)/len_comp)
            cuadro[i+1][j+1]=str(similitud)+"%"

def mostrar_cuadro(cuadro):
    print("Porcentaje de similitud de los genomas:")
    cuadro[0][0] = ' '
    for i in range(1, len(cuadro)):
        cuadro[i][0] = (os.path.split(files[i - 1]))[1]
    for j in range(1, len(cuadro)):
        cuadro[0][j] = (os.path.split(files[j - 1]))[1]
    for i in range(len(cuadro)):
        for j in range(len(cuadro)):
            print((cuadro[i][j]).center(15), end=' ')
            print("|", end='')
        print()

files = ["genomas/AY274119.txt",
            "genomas/AY278488.2.txt",
            "genomas/MN908947.txt",
            "genomas/MN988668.txt",
            "genomas/MN988669.txt"]

cuadro = [[0]*(len(files)+1) for i in range(len(files)+1)]
comparison(files, cuadro)
mostrar_cuadro(cuadro)




