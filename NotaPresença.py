import tkinter as tk
from tkinter import messagebox

def verificar_aprovacao():
    try:
        nota = float(entry_nota.get())
        frequencia = float(entry_frequencia.get())

        if nota >= 7.0 and frequencia >= 75:
            resultado_var.set("Aluno aprovado!")
        else:
            resultado_var.set("Aluno reprovado.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos.")

# Janela principal
app = tk.Tk()
app.title("Verificar Aprovação")
app.geometry("300x300")
app.configure(bg="#f5f5f5")

# Título
titulo = tk.Label(app, text="Verificar Aprovação", font=("Arial", 16, "bold"), bg="#f5f5f5")
titulo.pack(pady=10)

# Entrada de nota
entry_nota = tk.Entry(app)
entry_nota.pack(pady=5)
entry_nota.insert(0, "Digite a nota do aluno")

# Entrada de frequência
entry_frequencia = tk.Entry(app)
entry_frequencia.pack(pady=5)
entry_frequencia.insert(0, "Digite a frequência (%)")

# Botão de verificação
botao = tk.Button(app, text="Verificar", command=verificar_aprovacao)
botao.pack(pady=10)

# Resultado
resultado_var = tk.StringVar()
resultado_label = tk.Label(app, textvariable=resultado_var, font=("Arial", 14), bg="#f5f5f5")
resultado_label.pack(pady=10)

# Inicia o loop da interface
app.mainloop()
