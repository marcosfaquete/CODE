import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        sg.change_look_and_feel('DarkBrown4')
        # Layout
        layout = [
            [sg.Text('Nome',size=(5,0)),sg.Input(size=(15,0),key='Nome')],
            [sg.Text('Idade',size=(5,0)),sg.Input(size=(15,0),key='Idade')],
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail',key='Gmail'),sg.Checkbox('Outlook',key='Outlook'),sg.Checkbox('Yahoo',key='Yahoo')],
            [sg.Text('Aceita cartão')],
            [sg.Radio('Sim', 'cartoes',key='aceitaCartao'),sg.Radio('Não','cartoes',key='naoAceitaCartao')],
            [sg.Slider(range=(0,255),default_value=0,orientation='h',size=(15,20),key='sliderVelocidade')],
            [sg.Button('Enviar Dados')],

            [sg.Output(size=(30,10))]
        ]
        # Janela
        self.janela = sg.Window("Dados do Usuário").layout(layout)
        # Extrair os dados da tela
        
    
    def Iniciar(self):
        while True:
            # Extraindo os dados da tela
            self.button, self.values = self.janela.Read()

            print('\n')
            nome = self.values['Nome']
            idade = self.values['Idade']
            aceita_gmail = self.values['Gmail']
            aceita_outlook = self.values['Outlook']     # Passando para variável
            aceita_yahoo = self.values['Yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']

            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')  # Printando na tela
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'Aceita Cartão: {aceita_cartao}')
            print(f'Não aceita Cartão: {nao_aceita_cartao}')
            print(f'Velocidade Scripts: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()
    

