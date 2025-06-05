import tkinter as tk
from tkinter import messagebox # Importa a biblioteca tkinter para criar a interface gráfica e a biblioteca messagebox para exibir mensagens de erro.

# função para converter decimal para binário
def decimal_para_binario():
    try:
        decimal = int(entrada_decimal.get())
        entrada_binario.delete(0, tk.END)
        entrada_binario.insert(0, bin(decimal)[2:]) # Converte o número decimal para binário e remove o prefixo '0b'.
    except ValueError:
        messagebox.showerror("Erro", "Digite um número decimal válido.") # Trata erros de conversão de decimal para binário.

# função para converter binário para decimal
def binario_para_decimal():
    try:
        binario_str = entrada_binario.get()
        decimal = int(binario_str, 2)
        entrada_decimal.delete(0, tk.END)
        entrada_decimal.insert(0, str(decimal))
    except ValueError:
        messagebox.showerror("Erro", "Digite um número binário válido.") # Trata erros de conversão de binário para decimal.

# Cria a janela principal da aplicação
janela = tk.Tk()
janela.title("Conversor Decimal/Binário")

# Decimal para Binário
rotulo_decimal = tk.Label(janela, text="Decimal:")
rotulo_decimal.grid(row=0, column=0, padx=5, pady=5)
entrada_decimal = tk.Entry(janela)
entrada_decimal.grid(row=0, column=1, padx=5, pady=5)

# Botão para converter Decimal para Binário
botao_dec_para_bin = tk.Button(janela, text="→ Binário", command=decimal_para_binario)
botao_dec_para_bin.grid(row=0, column=2, padx=5, pady=5)

# Binário para Decimal
rotulo_binario = tk.Label(janela, text="Binário:")
rotulo_binario.grid(row=1, column=0, padx=5, pady=5)
entrada_binario = tk.Entry(janela)
entrada_binario.grid(row=1, column=1, padx=5, pady=5)

# Botão para converter Binário para Decimal
botao_bin_para_dec = tk.Button(janela, text="→ Decimal", command=binario_para_decimal)
botao_bin_para_dec.grid(row=1, column=2, padx=5, pady=5)

janela.mainloop()