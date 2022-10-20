import tkinter as tk
from tkinter import ttk
import datetime as dt


lista_tipo = ["Galao", "Caixa", "Saco", "Unidade"]
lista_codigos = []
janela = tk.Tk()

#criacao da funcao
def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = comboBox_selecionar_tipo.get()
    quant = entry_quant.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%Y %H:%M:%S")
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str, descricao, tipo, quant, data_criacao ))


#titulo da janela
janela.title("ferramenta de cadastro de materiais")

#descicao para o rotulo do material que queremos
label_descricao = tk.Label(text = "Descricao do material")
label_descricao.grid(row=1, column=0, padx=10, pady= 10, sticky="nswe", columnspan=4)


entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, sticky='nswe', columnspan=4)

label_unidade = tk.Label(text="Tipo da unidade do material")
label_unidade.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

comboBox_selecionar_tipo = ttk.Combobox(values=lista_tipo)
comboBox_selecionar_tipo.grid(row=3, column=2, pady=10, padx=10, sticky="nswe", columnspan=2)

label_quant = tk.Label(text="quantidade na unidade de material")
label_quant.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

entry_quant = tk.Entry()
entry_quant.grid(row=4, column=2, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_criar_codigo = tk.Button(text="criar codigo", command=inserir_codigo)
botao_criar_codigo.grid(row=5, column=0, padx=10, pady=10, sticky="nswe", columnspan=4)

janela.mainloop()

print(lista_codigos)
