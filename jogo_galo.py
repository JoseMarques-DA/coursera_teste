import tkinter as tk
from tkinter import messagebox

class JogoGalo:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo do Galo")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Variáveis do jogo
        self.jogador_atual = "X"
        self.tabuleiro = [""] * 9
        self.jogo_ativo = True
        
        # Criar interface
        self.criar_interface()
        
    def criar_interface(self):
        # Título
        titulo = tk.Label(
            self.root,
            text="JOGO DO GALO",
            font=("Arial", 32, "bold"),
            bg="#2c3e50",
            fg="white"
        )
        titulo.pack(pady=30)
        
        # Frame para o jogador atual
        self.jogador_frame = tk.Frame(self.root, bg="#2c3e50")
        self.jogador_frame.pack(pady=10)
        
        self.jogador_label = tk.Label(
            self.jogador_frame,
            text=f"Jogador: {self.jogador_atual}",
            font=("Arial", 20, "bold"),
            bg="#2c3e50",
            fg="#3498db"
        )
        self.jogador_label.pack()
        
        # Frame para o tabuleiro
        tabuleiro_frame = tk.Frame(self.root, bg="#34495e")
        tabuleiro_frame.pack(pady=30)
        
        # Criar botões do tabuleiro
        self.botoes = []
        for i in range(3):
            for j in range(3):
                btn = tk.Button(
                    tabuleiro_frame,
                    text="",
                    font=("Arial", 28, "bold"),
                    width=6,
                    height=3,
                    bg="#34495e",
                    fg="white",
                    relief="flat",
                    command=lambda row=i, col=j: self.fazer_jogada(row, col)
                )
                btn.grid(row=i, column=j, padx=3, pady=3)
                self.botoes.append(btn)
        
        # Botão de reiniciar
        reiniciar_btn = tk.Button(
            self.root,
            text="Reiniciar Jogo",
            font=("Arial", 18, "bold"),
            bg="#e74c3c",
            fg="white",
            relief="flat",
            command=self.reiniciar_jogo
        )
        reiniciar_btn.pack(pady=30)
        
    def fazer_jogada(self, row, col):
        if not self.jogo_ativo:
            return
            
        index = row * 3 + col
        
        if self.tabuleiro[index] == "":
            # Fazer a jogada
            self.tabuleiro[index] = self.jogador_atual
            self.botoes[index].config(
                text=self.jogador_atual,
                bg="#3498db" if self.jogador_atual == "X" else "#e74c3c"
            )
            
            # Verificar se há vencedor
            if self.verificar_vencedor():
                messagebox.showinfo("Fim do Jogo", f"Jogador {self.jogador_atual} venceu!")
                self.jogo_ativo = False
                return
            
            # Verificar empate
            if "" not in self.tabuleiro:
                messagebox.showinfo("Fim do Jogo", "Empate!")
                self.jogo_ativo = False
                return
            
            # Trocar jogador
            self.jogador_atual = "O" if self.jogador_atual == "X" else "X"
            self.jogador_label.config(text=f"Jogador: {self.jogador_atual}")
    
    def verificar_vencedor(self):
        # Linhas horizontais
        for i in range(0, 9, 3):
            if (self.tabuleiro[i] == self.tabuleiro[i+1] == self.tabuleiro[i+2] != ""):
                self.destacar_vencedor([i, i+1, i+2])
                return True
        
        # Linhas verticais
        for i in range(3):
            if (self.tabuleiro[i] == self.tabuleiro[i+3] == self.tabuleiro[i+6] != ""):
                self.destacar_vencedor([i, i+3, i+6])
                return True
        
        # Diagonais
        if (self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != ""):
            self.destacar_vencedor([0, 4, 8])
            return True
        
        if (self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != ""):
            self.destacar_vencedor([2, 4, 6])
            return True
        
        return False
    
    def destacar_vencedor(self, indices):
        for index in indices:
            self.botoes[index].config(bg="#27ae60")
    
    def reiniciar_jogo(self):
        # Resetar variáveis
        self.jogador_atual = "X"
        self.tabuleiro = [""] * 9
        self.jogo_ativo = True
        
        # Resetar interface
        for btn in self.botoes:
            btn.config(text="", bg="#34495e")
        
        self.jogador_label.config(text=f"Jogador: {self.jogador_atual}")

def main():
    root = tk.Tk()
    app = JogoGalo(root)
    root.mainloop()

if __name__ == "__main__":
    main()
