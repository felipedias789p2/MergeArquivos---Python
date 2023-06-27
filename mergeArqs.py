import os
from pathlib import Path
import os


# Função Recursiva para Checar se o arquivo existe no diretório
def checarArquivo(pathFile):
    arquivo = Path(pathFile)
    if arquivo.is_file():
        return pathFile
    else:
        novoArquivo = str(input("O arquivo não existe, digite um novo arquivo: \n"))
        novoArquivo.lstrip()
        return checarArquivo(novoArquivo)

nomesArquivos = []
linhasArqs = []
# while var != 'n':
while True:
    lerArquivo = str(input("Digite o nome do arquivo\n"))
    lerArquivo = checarArquivo(lerArquivo)
    nomesArquivos.append(lerArquivo)
    var = str(input("Deseja continuar?")).strip().upper()
    if var == 'N':
        break
nomeArqCriado = str(input("Digite o nome do arquivo que deseja criar\n"))
tol = open(nomeArqCriado, 'a')
for arquivos in nomesArquivos:
    arq = open(arquivos)
    linhas = arq.readlines()
    for linha in linhas:
        teste = linha.replace("\n", "")
        linhasArqs.append(teste)
listaUnica = list(set(linhasArqs))
listaUnica.sort()
numRegistros = len(listaUnica)
for arquivosMerge in listaUnica:
    tol.write(arquivosMerge +"\n")
print(f"Merge no arquivo {nomeArqCriado} Contém",numRegistros, "Registros")
tol.close()
arq.close()
os.system("pause")

