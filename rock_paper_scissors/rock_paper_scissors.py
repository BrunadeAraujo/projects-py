import random

user_points = 0
computer_points = 0
# Inicializa as pontuações do usuário e do computador como 0.

options = ["r", "t", "p"]

while True:
    # Inicia um loop infinito até o jogador decidir sair.
    user_choice = input("Escolha R(Pedra)/T(Tesoura)/P(Papel) ou Q para sair.").lower()

    if user_choice == 'q':
    # Se o usuário digitar 'q', o loop é encerrado.
      break

    if user_choice not in options:
       continue

    # Gera um número aleatório entre 0 e 2, representando a escolha do computador.
    computer_choice = random.randint(0,2)
    #0 : R, 1 : T, 2:P
    computer_option = options[computer_choice]
    # Associa o número aleatório a uma opção correspondente da lista `options`.

    print("O computador escolheu" + computer_option)
    
    if user_choice == computer_choice:
       print("Empate!")

    elif user_choice == "r" and computer_choice == "t":
       print("voce ganhou!")
       user_points = user_points + 1
      # Incrementa a pontuação do usuário.

    elif user_choice == "p" and computer_choice == "r":
       print("voce ganhou!")
       user_points = user_points + 1

    elif user_choice == "t" and computer_choice == "p":
       print("voce ganhou!")
       user_points = user_points + 1
       # Incrementa a pontuação do computador.
       
    else:
       print("voce perdeu!")
       computer_points = computer_points + 1

print("Sua pontuação:" + str(user_points))
print("Pontuação do Computador:" + str(computer_points))

if computer_points > user_points:
   print("Derrota!")
elif computer_points == user_points:
   print("Empate!")
else:
   print("Vitória")
   
print("Goodbye!")