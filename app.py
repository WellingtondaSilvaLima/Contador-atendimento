from tkinter import *
from tkinter import messagebox
import pyperclip as pc

# ------------- Configurações da Tela -----------------
janela = Tk()
largura = 355
altura = 580

icon = PhotoImage(file='imagens/icone.png')

janela.title('Contador de Atendimento')
janela.iconphoto(False, icon)
janela.geometry(f'{largura}x{altura}')
janela.resizable(False, False)
janela.configure(bg='#2F506D')
# -----------------------------------------------------

# ------------------------------ Online ------------------------------
titulo_online_label = Label(janela,
                            text='Online',
                            font=('Lucida Sans Unicode', 16, 'bold'),
                            fg='#fff',
                            bg='#2F506D')
titulo_online_label.grid(row=0, column=0, columnspan=4, pady=5)

class Online:
  def __init__(self, descricao) -> None:
    self.descricao = descricao
  
  def cria_label(self, linha:int, coluna_label:int, coluna_contador:int) -> None:
    label = Label(janela,
                  text=f'{self.descricao}',
                  font=('Lucida Sans Unicode', 12),
                  fg='#fff',
                  bg='#2F506D')
    label.grid(sticky='w', row=linha, column=coluna_label, padx=3, pady=5)

    self.contador = Label(janela,
                     text='0',
                     font=('Lucida Sans Unicode', 12),
                     fg='#fff',
                     bg='#2F506D')
    self.contador.grid(sticky='w', row=linha, column=coluna_contador, padx=30, pady=5)
  
  def cria_botoes(self, linha:int, coluna_mais:int, coluna_menos:int) -> None:
    btn_mais_um = Button(janela,
                         text='+',
                         width=3,
                         height=2,
                         command= lambda: self.soma())
    btn_mais_um.grid(row=linha, column=coluna_mais, padx=3, pady=5)

    btn_menos_um = Button(janela,
                          text='-',
                          width=3,
                          height=2,
                          bg='#fff',
                         command= lambda: self.subtracao())
    btn_menos_um.grid(row=linha, column=coluna_menos, padx=3, pady=5)


  def soma(self):
    contador = int(self.contador['text'])
    resultado = contador + 1
    self.contador['text'] = str(resultado)

  
  def subtracao(self):
    contador = int(self.contador['text'])
    if contador != 0:
      resultado = contador - 1
      self.contador['text'] = str(resultado)

  
  def pega_quantidade(self):
    return self.contador['text']



# =================== Liberação de online ===================
liberacao_online = Online('Liberação Online')
liberacao_online.cria_label(1, 0, 1)
liberacao_online.cria_botoes(1, 2, 3)
# ===========================================================

# ================== Recuperação de senha ===================
recuperacao_senha = Online('Recuperação de Senha')
recuperacao_senha.cria_label(2, 0, 1)
recuperacao_senha.cria_botoes(2, 2, 3)
# ===========================================================

# =================== Correção de pacote ====================
correcao_pacote = Online('Correção de Pacote')
correcao_pacote.cria_label(3, 0, 1)
correcao_pacote.cria_botoes(3, 2, 3)
# ===========================================================

# ========================= Outros ==========================
outros = Online('Outros')
outros.cria_label(4, 0, 1)
outros.cria_botoes(4, 2, 3)
# ===========================================================


# ------------------------------ Offline ------------------------------
titulo_online_label = Label(janela,
                            text='Offline',
                            font=('Lucida Sans Unicode', 16, 'bold'),
                            fg='#fff',
                            bg='#2F506D')
titulo_online_label.grid(row=5, column=0, columnspan=4, pady=5)

class Offline:
  def __init__(self, descricao) -> None:
    self.descricao = descricao
  
  def cria_label_off(self, linha:int, coluna_label:int, coluna_contador:int) -> None:
    label = Label(janela,
                  text=f'{self.descricao}',
                  font=('Lucida Sans Unicode', 12),
                  fg='#fff',
                  bg='#2F506D')
    label.grid(sticky='w', row=linha, column=coluna_label, padx=3, pady=5)

    self.contador = Label(janela,
                     text='0',
                     font=('Lucida Sans Unicode', 12),
                     fg='#fff',
                     bg='#2F506D')
    self.contador.grid(sticky='w', row=linha, column=coluna_contador, padx=30, pady=5)
  
  def cria_botoes_off(self, linha:int, coluna_mais:int, coluna_menos:int) -> None:
    btn_mais_um = Button(janela,
                         text='+',
                         width=3,
                         height=2,
                         command= lambda: self.soma())
    btn_mais_um.grid(row=linha, column=coluna_mais, padx=3, pady=5)

    btn_menos_um = Button(janela,
                          text='-',
                          width=3,
                          height=2,
                         command= lambda: self.subtracao())
    btn_menos_um.grid(row=linha, column=coluna_menos, padx=3, pady=5)

  def soma(self):
    contador = int(self.contador['text'])
    resultado = contador + 1
    self.contador['text'] = str(resultado)

  
  def subtracao(self):
    contador = int(self.contador['text'])
    if contador != 0:
      resultado = contador - 1
      self.contador['text'] = str(resultado)

  def pega_quantidade(self):
    return self.contador['text']


# ================== Instalação nova versão =================
instalacao_nova = Offline('Instalação nova')
instalacao_nova.cria_label_off(6, 0, 1)
instalacao_nova.cria_botoes_off(6, 2, 3)
# ===========================================================

# ====================== Reinstalação =======================
reinstalacao = Offline('Reinstalação')
reinstalacao.cria_label_off(7, 0, 1)
reinstalacao.cria_botoes_off(7, 2, 3)
# ===========================================================

# =================== Correção de manual ====================
correcao_manual = Offline('Correção de manual')
correcao_manual.cria_label_off(8, 0, 1)
correcao_manual.cria_botoes_off(8, 2, 3)
# ===========================================================

# ======================== Registro =========================
registro = Offline('Registro')
registro.cria_label_off(9, 0, 1)
registro.cria_botoes_off(9, 2, 3)
# ===========================================================


# ------------------------------ Nome e Gerar ------------------------------
def gerar(nome:Entry,
          liberacao_online:object, recuperacao_senha:object, correcao_pacote:object, outros:object,
          instalacao_nova:object, reinstalacao:object, correcao_manual:object, registro:object):
  entrada = nome
  nome = nome.get()
  quantidade_liberacao = liberacao_online.pega_quantidade()
  quantidade_recuperacao = recuperacao_senha.pega_quantidade()
  quantidade_correcao_pacote = correcao_pacote.pega_quantidade()
  quantidade_outros = outros.pega_quantidade()
  quantidade_instalacao = instalacao_nova.pega_quantidade()
  quantidade_reinstalacao = reinstalacao.pega_quantidade()
  quantidade_correcao_manual = correcao_manual.pega_quantidade()
  quantidade_registro = registro.pega_quantidade()
  total = int(quantidade_liberacao) + int(quantidade_recuperacao) + int(quantidade_correcao_pacote) + int(quantidade_outros) + int(quantidade_instalacao) + int(quantidade_reinstalacao) + int(quantidade_correcao_manual) + int(quantidade_registro)

  if nome == '':
    messagebox.showwarning(title='Dados incompletos', message='Digite seu nome para prosseguir.')
  else:
    texto = f'''Técnico {nome}
Liberações de Online: {quantidade_liberacao}
Recuperações de Senha: {quantidade_recuperacao}
Correções de Pacote: {quantidade_correcao_pacote}
Outros atendimentos: {quantidade_outros}

Instalações: {quantidade_instalacao}
Reinstalações: {quantidade_reinstalacao}
Correções de manuais: {quantidade_correcao_manual}
Registros Refeitos: {quantidade_registro}

Total de atendimentos: {total}
'''

    pc.copy(texto)

    entrada.delete(0, END)




nome = Entry(janela,
             bg='#fff',
             border=1,
             width=40)
nome.grid(row=10, column=0, columnspan=3, padx=5, pady=25, sticky='w')

btn_gerar = Button(janela,
                   text='Gerar',
                   width=8,
                   height=2,
                   command= lambda: gerar(nome,
                                          liberacao_online, recuperacao_senha, correcao_pacote, outros,
                                          instalacao_nova, reinstalacao, correcao_manual, registro))
btn_gerar.grid(row=10, column=2, columnspan=2, padx=2, pady=25)


janela.mainloop()