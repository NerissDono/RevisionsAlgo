
def main():
    input = "/chemin/vers/.././du//caca/mou.png"
    listeChemins = input.split("/")
    output = []
    
    for i in listeChemins:
        if i == "..":
            output.pop()
            continue
        elif i == ".":
            continue
        elif i == "":
            continue
        elif i == "/":
            continue
        
        else:
            output.append(i+"/")
    if output:
        output[-1] = output[-1][:-1] 
    for i in output:
        print(i, end="")
main()
