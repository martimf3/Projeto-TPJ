# Projeto-TPJ

Scraggle: Get the Diamond to Win! GAME OF THE YEAR EDITION é um pequeno jogo platformer 2D criado no âmbito da UC de Tópicos de Programação para jogos pelos alunos
João Oliveira (98767) e Martim Fernandes (114863).

[Link do repositório](https://github.com/martimf3/Projeto-TPJ)

O jogo está escrito em Python, e utiliza ficheiros .csv como suporte para o desenho da área de jogo, editados com o software Tiled.

Padrões utilizados:

- Programação orientada a objetos: O jogo está segmentado em vários ficheiros .py de forma a manter os seus elementos individuais organizados e manter o código
                                   estruturado de uma maneira intuitiva
                                   
- Observer: Um contador de moedas está subscrito a um observador, e envia um sinal cada vez que uma moeda é apanhada. Depois faz update a uma representação visual
            da pontuação
            
- Máquina de estados: O jogador tem estados diferentes mediante o tipo de movimento que está a executar. A área de jogo em si tem 5 estados distintos (pre-main menu
                      credits, main menu, victory, game over)
                      
Funcionalidades de código:

- decoration.py

      Class Sky:
	    
      init: faz o load das imagens das partes de cima, do meio e de baixo do céu e aplica escala para preencherem o ecrã. cria uma lista com nuvens em posições 
            aleatórias para as desenhar na linha do horizonte (parte do meio do céu)
	    
      draw: método para chamar quando queremos desenhar o céu no ecrã
      
      Class Water:
      
      init: define a posição inicial + tamanho do tile + número de tiles a criar.	anima a quantidade de tiles na variável 'tile_x_amount' a partir da class 
            AnimatedTile. adiciona cada AnimatedTile à 'lista de sprites'  
	    
      draw: método para desenhar a água no ecrã

      Class Clouds:
	    
      init: importa todas as nuvens através da funcção import_folder. define as possíveis coordenadas para x e y, escolhe aleatoriamente a quantidade de nuvens. 
            escolher uma imagem de nuvem aleatoriamente e atribui uma posição como sprite á lista de sprites
            
      draw: método para desenhar as nuvens no ecrã

- enemy.py

      Class Enemy:
      
      Extende a Class AnimatedTile

      init: chama-se super() para passar os argumentos da class AnimatedTile.	define uma variável para declarar a posição y do rect da imagem e uma para a velocidade	
	
      move: adiciona-se à cordenada x a velocidade para executar o movimento

      reverse_image: método para fazer flip à imagem quando o inimigo está a andar para a direita

      reverse: multiplica o speed por -1 para que o inimigo mude de direção
      
      update: atualiza a posição do inimigo quando quando a câmara se desloca. anima através da função animate da class AnimatedTile.	aplica a função de movimento.
              vira a imagem com a função reverse_image

- game_data.py

      Ficheiro com a informação dos elementos de nível em .csv
	
- main.py

      Class Game:

      init:	inicializa variáveis e o objeto overworld e define o estado atual
      
      create_level: inicializa o objeto level e define o estado atual para 'level'
       
      create_overworld: retorna o jogador ao menu principal via mudança de estado para 'overworld'
       
      change_coins: adiciona a variável 'amount' à contagem de moedas
       
      change_health:	altera a variável de contagem de HP com o 'amount' passado na função
      
      check_game_over:	verifica as condições de game_over
	
      run: verifica o estado e chama a função run do objeto (level, overworld, victory ou game_over) que estiver ativo.	caso se execute level.run chama 
           também as funções para desenhar a UI no ecra


- settings.py

      Ficheiro que contem os valores de opções da janela de jogo e grelha

- support.py

      Ficheiro que contém as funções de suporte para import dos assets

      import_folder: função que dá import a todos os assets de um pasta e os adiciona a uma lista
	
      import_csv_layout: função que importa os dados do ficheiro .csv do nivel usados para importar o ficheiro de dados do terreno
	
      import_cut_graphics: segmenta a imagem do tileset

- tiles.py

      Class Tile:
      
      init: inicializa as variáveis image e rect
	
      update:	muda a coordenada x do rectângulo para acompanhar o shift da câmara
      
      Class StaticTile:

      Extende a class Tile. atualiza a surface para uma passada na inicialização do objeto

      Class AnimatedTile:
      
      Extende a class Tile
      
      init:	importa os assets de uma pasta para uma lista atavés da funcão de support import_folder. inicializa-se a variável 'frame_index'	e a variável 'image' que 
            representa um asset da lista com o index = frame_index
	
      animate: a cada frame que passa adiciona-se 0.15(animation speed) ao frame_index para converter para inteiro e ir devolvendo o sprite da lista com o dado index
      
      update:	chama a função animate para executar a animação.	atualiza-se a posição x com o shift da câmara

      Class Coin:

      Extende a class AnimatedTile
	
      init:	atualiza a posição do centro do rect. define-se a variável value (valor da moeda)

      Class Palm:
      
      Extende a class AnimatedTile
      
      init:	atribui um offset para reposicionar a imagem

- ui.py

      init:	inicializa as variáveis necessárias.faz o load das imagens dos elementos do UI
      
      show_health: desenha a imagem. calcula o rácio de HP para calcular a largura da barra. desenha um rectângulo vermelho para representar a percentagem de HP atual
      
      show_coins:	desenha a imagem. renderiza a quantidade de coins passada na função. atualiza o rect da contagem.	desenha a contagem no ecrã
    
- level.py
 
      Class Level:
      
      init: inicializa as propriedades das variáveis necessárias à criação do nível, nomeadamente áudio, interpretação dos ficheiros .csv para desenhar na área de
            jogo e as localizações das nuvens
            
      create_tile_group: atribui os assets dos tilesets aos respetivos layouts
      
      player_setup: atribui os assets do jogador ao layout
      
      enemy_collision_reverse: causa a mudança de direção de um inimigo quando este chega a um limite definido via .csv
      
      create_jump_particles: cria partículas quando o jogador salta
      
      horizontal_movement_collision: gere colisões horizontais com o terreno
      
      vertical_movement_collision: gere colisões verticais e aplica gravidade
      
      scroll_x: simulação de movimento de câmara
      
      get_player_on_ground: verifica se o jogador está em contacto com o terreno ou não
      
      create_landing_dust: cria partículas quando o jogador aterra
      
      check_death: verifica se o HP do jogador chegou a 0, ou o mesmo caiu na água
      
      check_win: verifica se o jogador cumpriu os requisitos para vencer o jogo
      
      check_coin_collisions: verifica se o jogador colidiu com uma moeda e altera a pontuação
      
      check_enemy_collisions: verifica se os inimigos colidiram com o jogador. caso verticalmente, os inimigos desaparecem; caso horizontalmente, o jogador leva dano
      
      run: desenha os elementos na área de jogo, chamando as funções de draw e update. também verifica se o jogador morre ou vence o jogo
      
- player.py      

      Class Player:
      
      init: construtor que define a posição inicial do jogador, cria partículas quando são chamadas, gere o movimento, status e HP do jogador, e o áudio
      
      import_character_assets: aplica os assets necessários das animações do jogador
      
      import_dust_run_particles: aplica os assets necessários às partículas
      
      animate: faz loop às frames das respetivas animações quando estas são chamadas, mediante a velocidade da animação. atualiza os limites de colisão do jogador
               quando este muda de direção
               
      run_dust_animation: gere a animação das partículas de corrida, muda a direção quando necessário
      
      get_input: controlos do jogador
      
      get_status: atualiza o estado do jogador quando está no chão ou no ar
      
      apply_gravity: aplica gravidade
      
      jump: salta
      
      get_damage: verifica se o jogador está no período de invencibilidade. caso não esteja, leva dano
      
      invincibility_timer: gere o período de invencibilidade mediante o clock tick do jogo
      
      update: update do jogador
      

- overworld.py, game_over.py, victory_menu.py (são quase cópias uns dos outros)

      Class Overworld/Victory/Game_Over:
    
      init:	inicializa as variáveis e as funcões para setup, as imagens dos níveis e do ícone de seleção
   
      draw: desenha os elementos e opções no ecrã
    
      change_text_color: muda as cores das opções quando são selecionadas
    
      update: faz update quando há input do jogador
 
- coin_counter.py

      A classe CoinCounter é o subject e a classe CoinCounterDisplay é o observer. A instância do CoinCounter controla o número de moedas e notifica o
      CoinCounterDisplay sempre que a contagem de moedas muda. O CoinCounterDisplay atualiza o ecrâ com a contagem atual de moedas.
    
    
    
    
    
    
    
    
    
    
    
    
    
      
      
