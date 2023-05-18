import pyautogui
import time

screenWidth, screenHeight = pyautogui.size()    # Get the XY position of the mouse.
print('\n')
print('Resolução de Vídeo:', screenWidth,'x',screenHeight) # Mostra na tela a resolução.     
print('\n')
curretMouseX, currentMouseY = pyautogui.position()      # Get the XY position of the mouse.
print('Mouse Position', currentMouseY, currentMouseY)
print('\n')

pyautogui.alert(">>> Atenção, Não mova o mouse durante o desenho! <<<")

time.sleep(1)
pyautogui.press('win')

time.sleep(1)
pyautogui.write('paint')

time.sleep(1)
pyautogui.press('enter')

time.sleep(1)
pyautogui.hotkey('Ctrl' , 'e')

time.sleep(1)
pyautogui.write('1910')

time.sleep(1)
pyautogui.press('tab')

time.sleep(1)
pyautogui.write('880')

time.sleep(1)
pyautogui.press('enter')

pyautogui.moveTo(850, 475)

#[x]> Eixo Horizontal 
#[y]> Eixo Vertical
#[s]> Velocidade

               # X   Y  S
# X Positivo vai para DIREITA 
# X Negativo ESQUERDA 

# Y Positivo DESCE 
# Y Negativo SOBE 
         
pyautogui.drag(320, 0, 0.1)

pyautogui.drag(0, 170, 0.1)

pyautogui.drag(-320, 0, 0.1)

pyautogui.drag(0, -170, 0.1)

pyautogui.drag(160, -90, 0.1)

pyautogui.drag(160, 90, 0.1)

pyautogui.drag(0, 170, 0.1)

pyautogui.drag(-160, 90, 0.1)

pyautogui.drag(-160, -90, 0.1)

#Triangulo do meio Primeira parte subindo
pyautogui.drag(160, -258, 0.1)
#Triangulo do meio Segunda parte descendo
pyautogui.drag(160, 258, 0.1)
# Risco Meio descendo 3 Triangulo
pyautogui.drag(-160, 0, 0.1)
pyautogui.drag(0, 90, 0.1)

# RISCO MEIO MEDIDA
pyautogui.drag(159, -260, 0.1)       
pyautogui.drag(-318, 0, 0.1)
pyautogui.drag(159, 259, 0.1)
pyautogui.drag(0, -89, 0.1)
pyautogui.move(0, -258, 0.1)
pyautogui.drag(0, 88, 0.1)
pyautogui.move(158, 0, 0.1)
pyautogui.drag(-77, 43, 0.1)
pyautogui.move(79, 127, 0.1)

               # X   Y  S
# X Positivo vai para DIREITA 
# X Negativo ESQUERDA 

# Y Positivo DESCE 
# Y Negativo SOBE 

pyautogui.drag(-80, -40, 0.1)
pyautogui.move(-240, 40, 0.1)
pyautogui.drag(78, -40, 0.1)
pyautogui.move(-78, -130, 0.1)
pyautogui.drag(79, 42, 0.1)

# Outra etapa do desenho concluída.
# Iniciando etapa do desenho do triangulo interior virado para baixo.


               # X   Y  S
# X Positivo vai para DIREITA 
# X Negativo ESQUERDA 

# Y Positivo DESCE 
# Y Negativo SOBE 
pyautogui.drag(161, 0, 0.1)
pyautogui.drag(-80, 128, 0.1)
pyautogui.drag(-81, -128, 0.1)


# Iniciando o quarto triângulo
               # X   Y  S
# X Positivo vai para DIREITA 
# X Negativo ESQUERDA 

# Y Positivo DESCE 
# Y Negativo SOBE 
pyautogui.move(81, -42, 0.1)
pyautogui.drag(79, 129, 0.1 )
pyautogui.drag(-158, 0, 0.1)
pyautogui.drag(80, -130, 0.1)





























#pyautogui.moveTo(50, 150)
