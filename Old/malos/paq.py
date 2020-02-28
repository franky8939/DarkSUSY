def modificarLinea(archivo, buscar, reemplazar):
    with open(archivo, "r") as f:
        lines = (line.rstrip() for line in f)
        altered_lines = [reemplazar if line == buscar else line for line in lines]

    with open(archivo, "w") as f:
        f.write('\n'.join(altered_lines) + '\n')

