import time
import emoji
from playsound import playsound

emo = [':skull:', ':collision:', ':bust_in_silhouette:', ':evergreen_tree:', ':cloud:', ':ocean:']

def fim(name):
    print('\033[36m')
    print(f'Parabéns {name}')
    print('\033[m')

nome = str(input('Olá Aventureiro, nos informe o seu nome: '))
print(' ')

x = 1
for x in range(1, 21):
    print(emoji.emojize(emo[4]), end=' ')

print(emoji.emojize('\n---===≡≡≡:evergreen_tree: Welcome to the Island :evergreen_tree:≡≡≡===---'))

for x in range(1, 16):
    print(emoji.emojize(emo[5], variant='emoji_type', use_aliases=True), end=' ')

playsound('songs/praia.mp3')

print('')
input('\n Começar (enter)')
print('')
time.sleep(0)
print(emoji.emojize(':bust_in_silhouette: - Você é jovem aventureijo, desbravador dos mares ou melhor, o rei dos mares...'))
time.sleep(2)
print(emoji.emojize(':collision:  BOOOOMMMMM   :collision:'))
playsound('songs/explosao.mp3')
print(emoji.emojize(':bust_in_silhouette: - Você ouve um barulho '))
time.sleep(1)
print(emoji.emojize(':bust_in_silhouette: - Parece que sua história ja não começa muito bem... O navio colidiu com uma rocha submersa*'))
time.sleep(2)
print(emoji.emojize(':ocean::sailboat: O navio está afundando :ocean::sailboat:',  variant='emoji_type', use_aliases=True))
time.sleep(1)
print(emoji.emojize(':bust_in_silhouette: - Você abandona o barco e pula no mar aberto'))
time.sleep(1)
print(emoji.emojize(':bust_in_silhouette: - Por sorte, você avista uma ilha, e nada em sua direção'))
time.sleep(1)
print(emoji.emojize(':mount_fuji: Você conseguiu! Você chegou na ilha (a princípio deserta)'))
time.sleep(2)
print(emoji.emojize(':bust_in_silhouette: - Você está exausto, com fome e com sede, precisa fazer algo logo. [FOME: 80% ; SEDE: 70%]'))
time.sleep(2)
print('')
print('a) Desbravar a ilha'), time.sleep(0.4)
print('b) Sentar em uma sombra e descansar'), time.sleep(0.4)
print('c) Fazer um sinal de SOS para possíveis socorristas')
esc = str(input('- '))

if esc == 'a':
    print(emoji.emojize(':bust_in_silhouette: - Você adentra na ilha, por sorte você encontra :cherries: frutíferos e alguns :bug: insetos em volta...'))
    print('a) Comer os frutos'), time.sleep(0.4)
    print('b) Comer alguns insetos'), time.sleep(0.4)
    print('c) Seguir desbravando a ilha')
    esc = str(input('- '))
    if esc == 'a':
        print('\033[31m')
        print(emoji.emojize(':bust_in_silhouette: - Você come algumas frutinhas, porém você começa se sentir um pouco tonto, parece que eram frutas venenosas. Você morre envenenado. :skull:'))
        print('\033[m')
    if esc == 'c':
        print('\033[31m')
        print(emoji.emojize(':bust_in_silhouette: - Você continua desbravando a ilha, acaba encontrando um riacho,'))
        print(emoji.emojize('você mata a sua sede, porêm você está com muita fome e não tem mais energia para continuar. :skull:[FOME: 100%]'))
        print('\033[m')
    if esc == 'b':
        print(emoji.emojize(':bust_in_silhouette: - Por mais que :bug:insetos sejam nojentos, eles são proteina, então você come alguns insetos. [FOME: 60%] ')), time.sleep(2)
        print(emoji.emojize('Após comer e se sentir melhor, você decide se aventurar por dentro da ilha pra procurar recursos, porém')), time.sleep(2)
        print(emoji.emojize('Ao se aprofundar mais na ilha você se depara com três caminhos suspeitos')), time.sleep(1)
        print('a) Caminho 1 '), time.sleep(0.4)
        print('b) Caminho 2 '), time.sleep(0.4)
        print('c) Caminho 3 ')
        esc = str(input('- '))
        if esc == 'a':
            print('\033[31m')
            print(emoji.emojize(':bust_in_silhouette: - Você se depara com uma :leopard: onça que te ataca na hora, você não consegue escapar'))
            print('\033[m')
        if esc == 'b':
            print('\033[31m')
            print(emoji.emojize(':bust_in_silhouette: - Você encontra um coqueiro e tenta subir para pegar alguns cocos, quando você está prestes a alcançar os cocos,'))
            print('você escorrega de uma altura de 30 metros e acaba não resistindo. ')
            print('\033[m')
        if esc == 'c':
            print(emoji.emojize(':bust_in_silhouette: - Você se depara com uma horta cheia de raizes e vegetais, porém ouve barulhos*'))
            print('a) Se esconder'), time.sleep(0.4)
            print('b) Voltar para o caminho 2'), time.sleep(0.4)
            print('c) Pegar alguns alimentos da horta')
            esc = str(input('-'))
            if esc == 'b':
                print('\033[31m')
                print(emoji.emojize(':bust_in_silhouette: - Você encontra um coqueiro e tenta subir para pegar alguns cocos, quando você está prestes a')), time.sleep(2)
                print(emoji.emojize(' alcançar os cocos, você escorrega de uma altura de 30 metros e acaba não resistindo. :skull:'))
                print('\033[m')
            if esc == 'a':
                print(emoji.emojize(':bust_in_silhouette: - Você se esconde, fica observando e descobre que na ilha há alguns indígenas '))
                print('a) Pegar alguns alimentos da horta'), time.sleep(0.4)
                print('b)  Desistir, e voltar pelo caminho 1')
                esc = str(input('- '))
                if esc == 'b':
                    print('\033[31m')
                    print(emoji.emojize(':bust_in_silhouette: - Você se depara com uma onça que te ataca na hora, sem você ter reflexo para correr'))
                    print('\033[m')
                if esc == 'a':
                    print(emoji.emojize(':bust_in_silhouette: - você corre para tentar roubar alguns alimentos da horta, porém você é emboscado por dois índios que te leva como prisioneiro para a sua tribo ')), time.sleep(3)
                    print(emoji.emojize(':bust_in_silhouette: -  Você foi levado para a aldeia, e logo de cara é apresentado ao cacique da aldeia, para decidir o que irão fazer com você. *')), time.sleep(2)
                    print('a) Ser Corajoso'), time.sleep(0.4)
                    print('b) Ser Audacioso'), time.sleep(0.4)
                    print('c) Ser Consciente')
                    esc = str(input('-'))
                    if esc == 'a':
                        print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                        print('em sua conciencia você decide ser mais corajoso e logo que ele falou a primeira palavra você descarrega um cuspe'), time.sleep(2)
                        print('bem no meio da cara dele, querendo mostrar que não vai curvar a cabeça para ninguém, nem mesmo ao líder deles.'), time.sleep(2)
                        print('Porém na aldeia que você está, eles prezam pela harmonia e não aceitam esse tipo de desrepeito,'), time.sleep(2)
                        print('principalmente ainda pelo seu líder, então decidem torturá-lo até a morte enterrando você vivo. '), time.sleep(2)
                        print('\033[31m')
                        print('Você aguenta ainda um pouco, mas não demorou pra acontecer o inevitavel, infelizmente chegou o seu fim.'), time.sleep(2)
                        print('\033[m')
                    if esc == 'b':
                        print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                        print('após você explicar sobre quem você é ele decide enfim em te matar, porém você lança uma proposta. '), time.sleep(2)
                        print('A proposta é: uma luta entre vocês dois, se você ganhar se tornará o cacique da tribo e matará o atual, porém se você perder você será torturado até a morte.'), time.sleep(3)
                        print('O cacique ri da sua proposta pois ele se acha muito superior a ti, mas no fim aceita a proposta por diversão.'), time.sleep(2)
                        print('E que comece o combate :')
                        print(' ')

                        for x in range(1, 20):
                            print(emoji.emojize(emo[0]), end=' ')

                        print(emoji.emojize('\n:punch: :punch: :punch: :punch: :punch: :punch: ◀| O Duelo |▶ :punch: :punch: :punch: :punch: :punch: :punch:\n',variant='emoji_type', use_aliases=True), end='')

                        for x in range(1, 20):
                            print(emoji.emojize(emo[0]), end=' ')
                        playsound('songs/Boom.mp3')
                        print('')
                        print('')
                        input('\nO duelo começa ᗒ (enter)')
                        print('')

                        print(emoji.emojize('Cacique começa te atacando com um soco :crossed_swords:'))
                        time.sleep(1)
                        print('a) Revidar com um soco'), time.sleep(0.4)
                        print('b) Defender'), time.sleep(0.4)
                        print('c) Esquivar')
                        esc = str(input('- '))
                        if esc == 'a':
                            print(emoji.emojize('Em um combate de soco:punch: contra soco:punch:, o cacique é muito forte e você acaba quebrando seu pulso [ VIDA: 1/3 ]',variant='emoji_type', use_aliases=True))
                            time.sleep(3)
                            print('Com o seu pulso muito machucado, você agora está muito vulnerável a qualquer ataque')
                            time.sleep(2)
                            print('Agora o cacique salta em sua direção, em uma voadora mortal')
                            time.sleep(2)

                            print('a) Defender'), time.sleep(0.4)
                            print('b) Esquivar '), time.sleep(0.4)
                            print('c) Se render e mudar de propósta')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('\033[31m')
                                print(' Você tenta de defender da voadora de cacique, mas como você ja está vulnerável, você ja não aguenta mais essa batalha, e fica no chão [ VIDA: 0/3 ]')
                                print('\033[m')
                            if esc == 'b':
                                print('\033[31m')
                                print('Você consegue se esquivar da voadora, mas ja começa a sentir os efeitos da dor de um pulso quebrado e da fadiga'), time.sleep(2)
                                print(' O cacique continua a golpear e você tenta desviar, até que você perde por exaustão')
                                print('\033[m')
                            if esc == 'c':
                                print('Você se ve em um beco sem saída, com muita dor no pulso e cansado, você implora para eles te aceitarem como integrante da aldeia em vez de te matarem'), time.sleep(2)
                                print('\033[31m')
                                print('O cacique finje pensar em sua propósta mas a recusa na hora e te desfere varios golpes, até você não resistir mais')
                                print('\033[m')
                        if esc == 'b':
                            print('Você consegue defender, mas o cacique é forte e você acaba sofrendo alguns danos [ VIDA: 2/3  ]'), time.sleep(2)
                            print('Visto que você defendeu o soco do cacique, ele se prepara para te dar um chute')
                            print('a) Defender'), time.sleep(0.4)
                            print('b) Soco')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('O chute é certeiro na direcão da sua cabeça, por sorte você bloqueou com seu braço, mas mesmo assim, esse golpe te deixa levemente atordoado [ VIDA: 1/3 ]'), time.sleep(2)
                                print('O Cacique aproveita que você está levemente atordoado e pula em sua direção em uma voadora mortal')
                                print('a) Defender'), time.sleep(0.4)
                                print('b) Esquivar')
                                esc = str(input('- '))
                                if esc == 'a':
                                    print('\033[31m')
                                    print('O cacique é rapido e seus reflexos estão atordoados, você tenta defender'), time.sleep(1)
                                    print('mas os golpes do cacique te deixam muito ferido, sem forças, você perdeu o duelo. [ VIDA: 0/3 ] ')
                                    print('\033[m')
                                if esc == 'b':
                                    print('\033[31m')
                                    print('O cacique é rapido e seus reflexos estão atordoados, você toma uma voadora esmagadora no meio do peito e você não resiste [ VIDA: 0/3 ]')
                                    print('\033[m')
                            if esc == 'b':
                                print('\033[31m')
                                print(' Você desfere um soco perfeito em direção a cabeça do cacique, mas antes que o golpe acerte,'), time.sleep(2)
                                print('o cacique acerta um chute bem nas suas costelas (parece que alguns ossos se quebraram) você não tem mais forças para se mover.')
                                print('\033[m')
                        if esc == 'c':
                            print(emoji.emojize(':bust_in_silhouette: - Você teve bons reflexos para esquivar do ataque  [ VIDA: 3/3 ]')), time.sleep(1)
                            print(emoji.emojize(' O cacique viu que você é um daqueles que fica correndo da luta e se estressa :rage: desferindo varios golpes rápidos:', variant='emoji_type', use_aliases=True))
                            print('a) Esquivar'), time.sleep(0.4)
                            print('b) Revidar com golpes e defesa')
                            esc = str(input('- '))
                            if esc == 'b':
                                print(emoji.emojize('Um duelo intenso foi travado, chutes, socos :punch:, bloqueios :no_good:', variant='emoji_type', use_aliases=True))
                                playsound('songs/Fight.mp3')
                                print('porém o cacique é mais forte e seus ataques e defesas são menos efetivos do que os do cacique'), time.sleep(2)
                                print('Vocês dois ficam exaustos, mas dentre toda a poeira levantada pela intensa batalha...'), time.sleep(2)
                                print('\033[31m')
                                print(emoji.emojize('é você... que está caido no chão :skull:[ VIDA: 0/3 ]', variant='emoji_type', use_aliases=True))
                                print('\033[m')
                            if esc == 'a':
                                print(emoji.emojize(' Você fica um pouco cansado, mas consegue desviar de todos os golpes rapidos do cacique')), time.sleep(2)
                                print(emoji.emojize('Cacique fica muito furioso :rage: e usa todas as suas energias em um super chute aéreo,', variant='emoji_type', use_aliases=True)), time.sleep(2)
                                print('ele escala em uma árvore para pegar distância e salta em sua direção'), time.sleep(1)
                                print('a) Defender'), time.sleep(0.4)
                                print('b) Esquivar')
                                esc = str(input('- '))
                                if esc == 'a':
                                    print('\033[31m')
                                    print('Você vai confiante defender do super ataque do cacique, porém com a altura o golpe se torna tão poderoso que até o chão estremece,'), time.sleep(2)
                                    print('o cacique cai em cima de você com seu chute aéreo, você é completamente esmagado. [ VIDA: 0/3 ]')
                                    print('\033[m')
                                if esc == 'b':
                                    print('Cacique pula da arvore em sua direção, ele cai, levantando a terra do chão, mas você consegue desviar custando-lhe alguns arranhões.'), time.sleep(2)
                                    print('O cacique está exausto e ao mesmo tempo grita, pois torceu o tornozelo. Você ve uma chance de acabar com esse duelo.')
                                    print('a) gancho')
                                    input('- ')

                                    print('Você ve que o cacique não consegue mais se mover, e desfere um gancho perfeito'), time.sleep(2)
                                    print('bem no queixo do cacique, ele cai no chão inconsciente.'), time.sleep(1)
                                    print('Toda a aldeia se surpreende, porém foi uma batalha justa'), time.sleep(1)
                                    print('Você se torna o novo Cacique da aldeia.'), time.sleep(1)
                                    fim(nome)
                                    print('\033[36m')
                                    print(emoji.emojize(':checkered_flag: Welcome to the Island :checkered_flag:',variant='emoji_type', use_aliases=True))
                                    print('\033[m')
                                    playsound('songs/Vitoria.mp3')

                    if esc == 'c':
                        print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio')), time.sleep(2)
                        print('Você ve que está em minoria e decide agir conscientemente implorando pela sua vida e fazendo o que eles quiserem que você faça '), time.sleep(2)
                        print('\033[31m')
                        print('Você vive como escravo, trabalhando pelos interesse do cacique e da aldeia')
                        print('\033[m')
            if esc == 'c':
                print(emoji.emojize(':bust_in_silhouette: - Mesmo ouvindo barulhos estranhos, você corre para tentar roubar alguns alimentos da horta,')), time.sleep(2)
                print('porém você é emboscado por dois índios que te levam como prisioneiro para a sua tribo'), time.sleep(2)
                print('Você foi levado para a aldeia, e logo de cara é apresentado ao cacique da aldeia, para decidir o que irão fazer com você.'), time.sleep(2)
                print('a) Ser Corajoso'), time.sleep(0.4)
                print('b) Ser Audacioso'), time.sleep(0.4)
                print('c) Ser Consciente')
                esc = str(input('-'))
                if esc == 'a':
                    print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                    print('em sua conciencia você decide ser mais corajoso e logo que ele falou a primeira palavra você descarrega um cuspe'), time.sleep(2)
                    print('bem no meio da cara dele, querendo mostrar que não vai curvar a cabeça para ninguém, nem mesmo ao líder deles.'), time.sleep(2)
                    print('Porém na aldeia que você está, eles prezam pela harmonia e não aceitam esse tipo de desrepeito,'), time.sleep(2)
                    print('principalmente ainda pelo seu líder, então decidem torturá-lo até a morte enterrando você vivo. '), time.sleep(2)
                    print('\033[31m')
                    print('Você aguenta ainda um pouco, mas não demorou pra acontecer o inevitavel, infelizmente chegou o seu fim.')
                    print('\033[m')
                if esc == 'b':
                    print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                    print('após você explicar sobre quem você é ele decide enfim em te matar, porém você lança uma proposta.'), time.sleep(2)
                    print('A proposta é: uma luta entre vocês dois, se você ganhar se tornará o cacique da tribo e matará o atual, porém se você perder você será torturado até a morte.'), time.sleep(3)
                    print('O cacique ri da sua proposta pois ele se acha muito superior a ti, mas no fim aceita a proposta por diversão.'), time.sleep(2)
                    print('E que comece o combate ▶'), time.sleep(2)
                    print('')

                    for x in range(1, 20):
                        print(emoji.emojize(emo[0]), end=' ')

                    print(emoji.emojize('\n:punch: :punch: :punch: :punch: :punch: :punch: ◀| O Duelo |▶ :punch: :punch: :punch: :punch: :punch: :punch:\n',variant='emoji_type', use_aliases=True), end='')

                    for x in range(1, 20):
                        print(emoji.emojize(emo[0]), end=' ')
                    playsound('songs/Boom.mp3')
                    print('')
                    print('')
                    input('\nO duelo começa ᗒ (enter)')
                    print('')

                    print(emoji.emojize('Cacique começa te atacando com um soco :crossed_swords:'))
                    time.sleep(1)
                    print('a) Revidar com um soco'), time.sleep(0.4)
                    print('b) Defender'), time.sleep(0.4)
                    print('c) Esquivar')
                    esc = str(input('- '))
                    if esc == 'a':
                        print(emoji.emojize('Em um combate de soco:punch: contra soco:punch:, o cacique é muito forte e você acaba quebrando seu pulso [ VIDA: 1/3 ]',variant='emoji_type', use_aliases=True))
                        time.sleep(3)
                        print('Com o seu pulso muito machucado, você agora está muito vulnerável a qualquer ataque')
                        time.sleep(2)
                        print('Agora o cacique salta em sua direção, em uma voadora mortal')
                        time.sleep(2)

                        print('a) Defender'), time.sleep(0.4)
                        print('b) Esquivar '), time.sleep(0.4)
                        print('c) Se render e mudar de propósta')
                        esc = str(input('- '))
                        if esc == 'a':
                            print('\033[31m'), print(' Você tenta de defender da voadora de cacique, mas como você ja está vulnerável, você ja não aguenta mais essa batalha, e fica no chão [ VIDA: 0/3 ]'), print('\033[m')
                        if esc == 'b':
                            print('\033[31m'), print('Você consegue se esquivar da voadora, mas ja começa a sentir os efeitos da dor de um pulso quebrado e da fadiga'), time.sleep(2)
                            print(' O cacique continua a golpear e você tenta desviar, até que você perde por exaustão'), print('\033[m')
                        if esc == 'c':
                            print('Você se ve em um beco sem saída, com muita dor no pulso e cansado, você implora para eles te aceitarem como integrante da aldeia em vez de te matarem'), time.sleep(2)
                            print('\033[31m'), print('O cacique finje pensar em sua propósta mas a recusa na hora e te desfere varios golpes, até você não resistir mais'), print('\033[31m')

                    if esc == 'b':
                        print('Você consegue defender, mas o cacique é forte e você acaba sofrendo alguns danos [ VIDA: 2/3  ]'), time.sleep(2)
                        print('Visto que você defendeu o soco do cacique, ele se prepara para te dar um chute')
                        print('a) Defender'), time.sleep(0.4)
                        print('b) Soco')
                        esc = str(input('- '))
                        if esc == 'a':
                            print('O chute é certeiro na direcão da sua cabeça, por sorte você bloqueou com seu braço, mas mesmo assim, esse golpe te deixa levemente atordoado [ VIDA: 1/3 ]'), time.sleep(2)
                            print('O Cacique aproveita que você está levemente atordoado e pula em sua direção em uma voadora mortal')
                            print('a) Defender'), time.sleep(0.4)
                            print('b) Esquivar')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('\033[31m'), print('O cacique é rapido e seus reflexos estão atordoados, você tenta defender'), time.sleep(1)
                                print('mas os golpes do cacique te deixam muito ferido, sem forças, você perdeu o duelo. [ VIDA: 0/3 ] '), print('\033[m')
                            if esc == 'b':
                                print('\033[31m'), print('O cacique é rapido e seus reflexos estão atordoados, você toma uma voadora esmagadora no meio do peito, você não resiste [ VIDA: 0/3 ]'), print('\033[m')

                        if esc == 'b':
                            print('\033[31m'), print(' Você desfere um soco perfeito em direção a cabeça do cacique, mas antes que o golpe acerte,'), time.sleep(2)
                            print('o cacique acerta um chute bem nas suas costelas (parece que alguns ossos se quebraram) você não tem mais forças para se mover.'), print('\033[m')

                    if esc == 'c':
                        print(emoji.emojize(':bust_in_silhouette: - Você teve bons reflexos para esquivar do ataque  [ VIDA: 3/3 ]')), time.sleep(1)
                        print(emoji.emojize(' O cacique viu que você é um daqueles que fica correndo da luta e se estressa :rage: desferindo varios golpes rápidos:',variant='emoji_type', use_aliases=True))
                        print('a) Esquivar'), time.sleep(0.4)
                        print('b) Revidar com golpes e defesa')
                        esc = str(input('- '))
                        if esc == 'b':
                            print(emoji.emojize('Um duelo intenso foi travado, chutes, socos :punch:, bloqueios :no_good:',variant='emoji_type', use_aliases=True))
                            playsound('songs/Fight.mp3')
                            print('porém o cacique é mais forte e seus ataques e defesas são menos efetivos do que os do cacique'), time.sleep(2)
                            print('Vocês dois ficam exaustos, mas dentre toda poeira levantada pela intensa batalha...'), time.sleep(2)
                            print('\033[31m'), print(emoji.emojize('é você... que está caido no chão :skull:[ VIDA: 0/3 ]',variant='emoji_type', use_aliases=True)), print('\033[m')

                        if esc == 'a':
                            print(emoji.emojize(' Você fica um pouco cansado, mas consegue desviar de todos os golpes rapidos do cacique')), time.sleep(2)
                            print(emoji.emojize('Cacique fica muito furioso :rage: e usa todas as suas energias em um super chute aéreo,',variant='emoji_type', use_aliases=True)), time.sleep(2)
                            print('ele escala em uma árvore para pegar distância e salta em sua direção'), time.sleep(1)
                            print('a) Defender'), time.sleep(0.4)
                            print('b) Esquivar')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('\033[31m'), print('Você vai confiante defender do super ataque do cacique, porém com a altura o golpe se torna tão poderoso que até o chão estremece,'), time.sleep(3)
                                print('o cacique cai em cima de você com seu chute aéreo, você é completamente esmagado. [ VIDA: 0/3 ]'), print('\033[m')
                            if esc == 'b':
                                print('Cacique pula da arvore em sua direção, ele cai, levantando a terra do chão, mas você consegue desviar custando-lhe alguns arranhões.'), time.sleep(3)
                                print('O cacique está exausto e ao mesmo tempo grita, pois torceu o tornozelo. Você ve uma chance de acabar com esse duelo.'), time.sleep(2)
                                print('a) gancho')
                                input('- ')

                                print('Você ve que o cacique não consegue mais se mover, e desfere um gancho perfeito'), time.sleep(2)
                                print('bem no queixo do cacique, ele cai no chão inconsciente.'), time.sleep(1)
                                print('Toda a aldeia se surpreende, porém foi uma batalha justa'), time.sleep(1)
                                print('Você se torna o novo Cacique da aldeia.'), time.sleep(1)
                                fim(nome)
                                print('\033[36m')
                                print(emoji.emojize(':checkered_flag: Welcome to the Island :checkered_flag:',variant='emoji_type', use_aliases=True))
                                print('\033[m')
                                playsound('songs/Vitoria.mp3')
                ######################
                if esc == 'c':
                    print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio*	'))
                    print('Você ve que está em minoria e decide agir conscientemente implorando pela sua vida e fazendo o que eles quiserem que você faça')
                    print('\033[31m'), print('Você vive como escravo, trabalhando pelos interesse do cacique e da aldeia'), print('\033[m')


elif esc == 'b':
    print(emoji.emojize(':bust_in_silhouette: - Você senta na areia, em baixa da sombra de um coqueiro. Você está descansado, porêm a sua fome e sede aumentam [FOME: 90% ; SEDE: 75%]'))
    print('a) Desbravar a ilha'), time.sleep(0.4)
    print('b) Continuar descansando'), time.sleep(0.4)
    print('c) Beber água do mar')
    esc = str(input('-'))

    if esc == 'a':
        print(emoji.emojize(':bust_in_silhouette: - Você adentra na ilha, por sorte você encontra frutíferos e alguns insetos em volta...'))
        print('a) Comer os frutos'), time.sleep(0.4)
        print('b) Comer alguns insetos'), time.sleep(0.4)
        print('c) Seguir desbravando a ilha')
        esc = str(input('-'))
        if esc == 'a':
            print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você come algumas frutinhas, porém você começa se sentir um pouco tonto, parece que eram frutas venenosas. Você morre envenenado.')), print('\033[m')
        if esc == 'b':
            print('\033[31m'), print(emoji.emojize(' Por mais que insetos:bug: sejam nojentos, eles são proteina, então você come alguns insetos,'))
            print('porém você acaba comendo um inseto infectado que faz com que você passe muito mal e acabe morrendo.'), print('\033[m')
        if esc == 'c':
            print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você continua desbravando a ilha, acaba encontrando um riacho, você mata a sua sede, porêm você está com muita fome e não tem mais energia para continuar. [FOME: 100%]')), print('\033[m')

    if esc == 'b':
        print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você continua descansando porêm você está com muita fome e não tem mais energia para se levantar. [FOME: 100%] ')), print('\033[m')

    if esc == 'c':
        print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você bebeu a água do mar, após um tempo você sente sintomas de desidratação e morre. [SEDE: 100%]')), print('\033[m')

elif esc == 'c':
    print(emoji.emojize(':bust_in_silhouette: - Você coleta alguns itens que encontra pela ilha, como, gravetos, cipó, folhas e faz um grande sinal escrito "SOS". Isso lhe custou muita energia, porém você fez um bom trabalho! [ FOME: 95%  ;  SEDE: 90% ]*'))
    print('a) Construir sua cabana'), time.sleep(0.4)
    print('b) Esperar pela ajuda'), time.sleep(0.4)
    print('c) Desbravar a Ilha')
    esc = str(input('-'))
    if esc == 'a':
        print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você coleta alguns itens para construir sua cabana, porém você está no fim de suas energias. [ FOME: 100%  ;  SEDE: 100%] ')), print('\033[m')
    if esc == 'b':
        print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você acaba esperando tempo demais pela ajuda. Com fome e sede você não tem mais energia para se mover.  [ FOME: 100%  ;  SEDE: 100%] ')), print('\033[m')
    if esc == 'c':
        print(emoji.emojize(':bust_in_silhouette: -  você decide se aventurar por dentro da ilha pra procurar recursos, porém, ao se aprofundar mais na ilha você se depara com três caminhos suspeitos*'))
        print('a) Caminho 1 '), time.sleep(0.4)
        print('b) Caminho 2 '), time.sleep(0.4)
        print('c) Caminho 3 ')
        esc = str(input('-'))
        if esc == 'a':
            print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: -  Você se depara com uma onça que te ataca na hora, sem você ter reflexo para correr *')), print('\033[m')
        if esc == 'b':
            print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você encontra um coqueiro e tenta subir para pegar alguns cocos, quando você está prestes a alcançar os cocos, você escorrega de uma altura de 30 metros e acaba não resistindo. ')), print('\033[m')
        if esc == 'c':
            print(emoji.emojize(':bust_in_silhouette: - Você se depara com uma horta cheia de raizes e vegetais, porém ouve barulhos*'))
            print('a) Se esconder'), time.sleep(0.4)
            print('b) Voltar para o caminho 2'), time.sleep(0.4)
            print('c) Pegar alguns alimentos da horta')
            esc = str(input('-'))

            if esc == 'a':
                print(emoji.emojize(':bust_in_silhouette: - Você se esconde, fica observando e descobre que na ilha há alguns indígenas* '))
                print('a) Pegar alguns alimentos da horta'), time.sleep(0.4)
                print('b)  Desistir, e voltar pelo caminho 1')
                esc = str(input('-'))
                if esc == 'b':
                    print('\033[31m'), print(emoji.emojize(':bust_in_silhouette: - Você se depara com uma onça que te ataca na hora, sem você ter reflexo para correr')), print('\033[m')
                if esc == 'a':
                    print(emoji.emojize(':bust_in_silhouette: - Você corre para tentar roubar alguns alimentos da horta, porém você é emboscado por dois índios que te leva como prisioneiro para a sua tribo ')), time.sleep(2)
                    print('Você foi levado para a aldeia, e logo de cara é apresentado ao cacique da aldeia, para decidir o que irão fazer com você.')
                    print('a) Ser Corajoso'), time.sleep(0.4)
                    print('b) Ser Audacioso'), time.sleep(0.4)
                    print('c) Ser Consciente')
                    esc = str(input('-'))
                    if esc == 'a':
                        print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                        print('em sua conciencia você decide ser mais corajoso e logo que ele falou a primeira palavra você descarrega um cuspe'), time.sleep(2)
                        print('bem no meio da cara dele, querendo mostrar que não vai curvar a cabeça para ninguém, nem mesmo ao líder deles.'), time.sleep(2)
                        print('Porém na aldeia que você está, eles prezam pela harmonia e não aceitam esse tipo de desrepeito,'), time.sleep(2)
                        print('principalmente ainda pelo seu líder, então decidem torturá-lo até a morte enterrando você vivo. '), time.sleep(2)
                        print('\033[31m'), print('Você aguenta ainda um pouco, mas não demorou pra acontecer o inevitavel, infelizmente chegou o seu fim.'), print('\033[m')
                    if esc == 'b':
                        print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                        print('após você explicar sobre quem você é ele decide enfim em te matar, porém você lança uma proposta. '), time.sleep(2)
                        print('A proposta é: uma luta entre vocês dois, se você ganhar se tornará o cacique da tribo e matará o atual, porém se você perder você será torturado até a morte.'), time.sleep(3)
                        print('O cacique ri da sua proposta pois ele se acha muito superior a ti, mas no fim aceita a proposta por diversão.'), time.sleep(2)
                        print('E que comece o combate :')
                        print(' ')

                        for x in range(1, 20):
                            print(emoji.emojize(emo[0]), end=' ')

                        print(emoji.emojize('\n:punch: :punch: :punch: :punch: :punch: :punch: ◀| O Duelo |▶ :punch: :punch: :punch: :punch: :punch: :punch:\n',variant='emoji_type', use_aliases=True), end='')

                        for x in range(1, 20):
                            print(emoji.emojize(emo[0]), end=' ')
                        playsound('songs/Boom.mp3')
                        print('')
                        print('')
                        input('\nO duelo começa ᗒ (enter)')
                        print('')

                        print(emoji.emojize('Cacique começa te atacando com um soco :crossed_swords:'))
                        time.sleep(1)
                        print('a) Revidar com um soco'), time.sleep(0.4)
                        print('b) Defender'), time.sleep(0.4)
                        print('c) Esquivar')
                        esc = str(input('- '))
                        if esc == 'a':
                            print(emoji.emojize('Em um combate de soco:punch: contra soco:punch:, o cacique é muito forte e você acaba quebrando seu pulso [ VIDA: 1/3 ]',variant='emoji_type', use_aliases=True))
                            time.sleep(3)
                            print('Com o seu pulso muito machucado, você agora está muito vulnerável a qualquer ataque')
                            time.sleep(2)
                            print('Agora o cacique salta em sua direção, em uma voadora mortal')
                            time.sleep(2)

                            print('a) Defender'), time.sleep(0.4)
                            print('b) Esquivar '), time.sleep(0.4)
                            print('c) Se render e mudar de propósta')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('\033[31m'), print(' Você tenta de defender da voadora de cacique, mas como você ja está vulnerável, você ja não aguenta mais essa batalha, e fica no chão [ VIDA: 0/3 ]'), print('\033[m')
                            if esc == 'b':
                                print('Você consegue se esquivar da voadora, mas ja começa a sentir os efeitos da dor de um pulso quebrado e da fadiga'), time.sleep(2)
                                print('\033[31m'), print(' O cacique continua a golpear e você tenta desviar, até que você perde por exaustão'), print('\033[m')
                            if esc == 'c':
                                print('Você se ve em um beco sem saída, com muita dor no pulso e cansado, você implora para eles te aceitarem como integrante da aldeia em vez de te matarem'), time.sleep(2)
                                print('\033[31m'), print('O cacique finje pensar em sua propósta mas a recusa na hora e te desfere varios golpes, até você não resistir mais'), print('\033[m')

                        if esc == 'b':
                            print('Você consegue defender, mas o cacique é forte e você acaba sofrendo alguns danos [ VIDA: 2/3  ]'), time.sleep(2)
                            print('Visto que você defendeu o soco do cacique, ele se prepara para te dar um chute')
                            print('a) Defender'), time.sleep(0.4)
                            print('b) Soco')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('O chute é certeiro na direcão da sua cabeça, por sorte você bloqueou com seu braço, mas mesmo assim, esse golpe te deixa levemente atordoado [ VIDA: 1/3 ]'), time.sleep(2)
                                print('O Cacique aproveita que você está levemente atordoado e pula em sua direção em uma voadora mortal')
                                print('a) Defender'), time.sleep(0.4)
                                print('b) Esquivar')
                                esc = str(input('- '))
                                if esc == 'a':
                                    print('\033[31m'), print('O cacique é rapido e seus reflexos estão atordoados, você tenta defender'), time.sleep(1)
                                    print('mas os golpes do cacique te deixam muito ferido, sem forças, você perdeu o duelo. [ VIDA: 0/3 ] '), print('\033[m')
                                if esc == 'b':
                                    print('\033[31m'), print('O cacique é rapido e seus reflexos estão atordoados, você toma uma voadora esmagadora no meio do peito, você não resiste [ VIDA: 0/3 ]'), print('\033[m')

                            if esc == 'b':
                                print(' Você desfere um soco perfeito em direção a cabeça do cacique, mas antes que o golpe acerte,'), time.sleep(2)
                                print('\033[31m'), print('o cacique acerta um chute bem nas suas costelas (parece que alguns ossos se quebraram) você não tem mais forças para se mover.'), print('\033[m')

                        if esc == 'c':
                            print(emoji.emojize(':bust_in_silhouette: - Você teve bons reflexos para esquivar do ataque  [ VIDA: 3/3 ]')), time.sleep(1)
                            print(emoji.emojize(' O cacique viu que você é um daqueles que fica correndo da luta e se estressa :rage: desferindo varios golpes rápidos:', variant='emoji_type', use_aliases=True))
                            print('a) Esquivar'), time.sleep(0.4)
                            print('b) Revidar com golpes e defesa')
                            esc = str(input('- '))
                            if esc == 'b':
                                print(emoji.emojize('Um duelo intenso foi travado, chutes, socos :punch:, bloqueios :no_good:', variant='emoji_type', use_aliases=True))
                                playsound('songs/Fight.mp3')
                                print('porém o cacique é mais forte e seus ataques e defesas são menos efetivos do que os do cacique'), time.sleep(2)
                                print('Vocês dois ficam exaustos, mas dentre toda poeira levantada pela intensa batalha...'), time.sleep(2)
                                print('\033[31m'), print(emoji.emojize('é você... que está caido no chão :skull:[ VIDA: 0/3 ]', variant='emoji_type', use_aliases=True)), print('\033[m')

                            if esc == 'a':
                                print(emoji.emojize(' Você fica um pouco cansado, mas consegue desviar de todos os golpes rapidos do cacique')), time.sleep(2)
                                print(emoji.emojize('Cacique fica muito furioso :rage: e usa todas as suas energias em um super chute aéreo,', variant='emoji_type', use_aliases=True)), time.sleep(2)
                                print('ele escala em uma árvore para pegar distância e salta em sua direção'), time.sleep(1)
                                print('a) Defender'), time.sleep(0.4)
                                print('b) Esquivar')
                                esc = str(input('- '))
                                if esc == 'a':
                                    print('\033[31m'), print('Você vai confiante defender do super ataque do cacique, porém com a altura o golpe se torna tão poderoso que até o chão estremece,'), time.sleep(2)
                                    print('o cacique cai em cima de você com seu chute aéreo, você é completamente esmagado. [ VIDA: 0/3 ]'), print('\033[m')
                                if esc == 'b':
                                    print('Cacique pula da arvore em sua direção, ele cai, levantando a terra do chão, mas você consegue desviar custando-lhe alguns arranhões.'), time.sleep(2)
                                    print('O cacique está exausto e ao mesmo tempo grita, pois torceu o tornozelo. Você ve uma chance de acabar com esse duelo.')
                                    print('a) gancho')
                                    input('- ')

                                    print('Você ve que o cacique não consegue mais se mover, e desfere um gancho perfeito'), time.sleep(2)
                                    print('bem no queixo do cacique, ele cai no chão inconsciente.'), time.sleep(1)
                                    print('Toda a aldeia se surpreende, porém foi uma batalha justa'), time.sleep(1)
                                    print('Você se torna o novo Cacique da aldeia.'), time.sleep(1)
                                    print('\033[34m')
                                    print('O sinal de SOS que você tinha feito teve efeito e um navio cargueiro que estava passando por perto, viu o sinal de Socorro e foi em direção da ilha, '), time.sleep(2)
                                    print('Você acaba de se tornar Cacique de uma tribo, mas pode voltar para casa... Então, qual será sua proxima decisão?'), time.sleep(2)
                                    print('\033[m')
                                    fim(nome)
                                    print('\033[36m')
                                    print(emoji.emojize(':checkered_flag: Welcome to the Island :checkered_flag:',variant='emoji_type', use_aliases=True))
                                    print('\033[m')
                                    playsound('songs/Vitoria.mp3')
                    ######################
                    if esc == 'c':
                        print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio*	')), time.sleep(2)
                        print('Você ve que está em minoria e decide agir conscientemente implorando pela sua vida e fazendo o que eles quiserem que você faça *'), time.sleep(2)
                        print('\033[31m'), print('Você vive como escravo, trabalhando pelos interesse do cacique e da aldeia *'), print('\033[m')


            if esc == 'b':
                print(emoji.emojize(':bust_in_silhouette: - Você encontra um coqueiro e tenta subir para pegar alguns cocos, quando você está prestes a alcançar os cocos, você escorrega de uma altura de 30 metros e acaba não resistindo.'))
            if esc == 'c':
                print(emoji.emojize(':bust_in_silhouette: - Mesmo ouvindo barulhos estranhos, você corre para tentar roubar alguns alimentos da horta,')), time.sleep(2)
                print('porém você é emboscado por dois índios que te levam como prisioneiro para a sua tribo '), time.sleep(1)
                print('Você foi levado para a aldeia, e logo de cara é apresentado ao cacique da aldeia, para decidir o que irão fazer com você.')
                print('a) Ser Corajoso'), time.sleep(0.4)
                print('b) Ser Audacioso'), time.sleep(0.4)
                print('c) Ser Consciente')
                esc = str(input('-'))
                if esc == 'a':
                    print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                    print('em sua conciencia você decide ser mais corajoso e logo que ele falou a primeira palavra você descarrega um cuspe'), time.sleep(2)
                    print('bem no meio da cara dele, querendo mostrar que não vai curvar a cabeça para ninguém, nem mesmo ao líder deles.'), time.sleep(2)
                    print('Porém na aldeia que você está, eles prezam pela harmonia e não aceitam esse tipo de desrepeito,'), time.sleep(2)
                    print('principalmente ainda pelo seu líder, então decidem torturá-lo até a morte enterrando você vivo. '), time.sleep(2)
                    print('\033[31m'), print('Você ainda aguenta um pouco, mas não demorou pra acontecer o inevitavel, infelizmente chegou o seu fim.'), print('\033[m')
                if esc == 'b':
                    print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio,')), time.sleep(3)
                    print('após você explicar sobre quem você é ele decide enfim em te matar, porém você lança uma proposta. '), time.sleep(2)
                    print('A proposta é: uma luta entre vocês dois, se você ganhar se tornará o cacique da tribo e matará o atual, porém se você perder você será torturado até a morte.'), time.sleep(3)
                    print('O cacique ri da sua proposta pois ele se acha muito superior a ti, mas no fim aceita a proposta por diversão.'), time.sleep(2)
                    print('E que comece o combate :')
                    print('')
                    for x in range(1, 20):
                        print(emoji.emojize(emo[0]), end=' ')

                    print(emoji.emojize('\n:punch: :punch: :punch: :punch: :punch: :punch: ◀| O Duelo |▶ :punch: :punch: :punch: :punch: :punch: :punch:\n',variant='emoji_type', use_aliases=True), end='')

                    for x in range(1, 20):
                        print(emoji.emojize(emo[0]), end=' ')
                    playsound('songs/Boom.mp3')
                    print('')
                    print('')
                    input('\nO duelo começa ᗒ (enter)')
                    print('')

                    print(emoji.emojize('Cacique começa te atacando com um soco :crossed_swords:'))
                    time.sleep(1)
                    print('a) Revidar com um soco'), time.sleep(0.4)
                    print('b) Defender'), time.sleep(0.4)
                    print('c) Esquivar')
                    esc = str(input('- '))
                    if esc == 'a':
                        print(emoji.emojize('Em um combate de soco:punch: contra soco:punch:, o cacique é muito forte e você acaba quebrando seu pulso [ VIDA: 1/3 ]',variant='emoji_type', use_aliases=True))
                        time.sleep(3)
                        print('Com o seu pulso muito machucado, você agora está muito vulnerável a qualquer ataque')
                        time.sleep(2)
                        print('Agora o cacique salta em sua direção, em uma voadora mortal')
                        time.sleep(2)

                        print('a) Defender'), time.sleep(0.4)
                        print('b) Esquivar '), time.sleep(0.4)
                        print('c) Se render e mudar de propósta')
                        esc = str(input('- '))
                        if esc == 'a':
                            print('\033[31m'), print(' Você tenta de defender da voadora de cacique, mas como você ja está vulnerável, você ja não aguenta mais essa batalha, e fica no chão [ VIDA: 0/3 ]'), print('\033[m')
                        if esc == 'b':
                            print('\033[31m'), print('Você consegue se esquivar da voadora, mas ja começa a sentir os efeitos da dor de um pulso quebrado e da fadiga'), time.sleep(2)
                            print(' O cacique continua a golpear e você tenta desviar, até que você perde por exaustão'), print('\033[m')
                        if esc == 'c':
                            print('\033[31m'), print('Você se ve em um beco sem saída, com muita dor no pulso e cansado, você implora para eles te aceitarem como integrante da aldeia em vez de te matarem'), time.sleep(2)
                            print('O cacique finje pensar em sua propósta mas a recusa na hora e te desfere varios golpes, até você não resistir mais'), print('\033[m')
                    if esc == 'b':
                        print('Você consegue defender, mas o cacique é forte e você acaba sofrendo alguns danos [ VIDA: 2/3  ]'), time.sleep(2)
                        print('Visto que você defendeu o soco do cacique, ele se prepara para te dar um chute')
                        print('a) Defender'), time.sleep(0.4)
                        print('b) Soco')
                        esc = str(input('- '))
                        if esc == 'a':
                            print('O chute é certeiro na direcão da sua cabeça, por sorte você bloqueou com seu braço, mas mesmo assim, esse golpe te deixa levemente atordoado [ VIDA: 1/3 ]'), time.sleep(2)
                            print('O Cacique aproveita que você está levemente atordoado e pula em sua direção em uma voadora mortal')
                            print('a) Defender'), time.sleep(0.4)
                            print('b) Esquivar')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('\033[31m'), print('O cacique é rapido e seus reflexos estão atordoados, você tenta defender'), time.sleep(1)
                                print('mas os golpes do cacique te deixam muito ferido, sem forças, você perde o duelo. [ VIDA: 0/3 ] '), print('\033[m')
                            if esc == 'b':
                                print('\033[31m'), print('O cacique é rapido e seus reflexos estão atordoados, você toma uma voadora esmagadora no meio do peito, você não resiste [ VIDA: 0/3 ]'), print('\033[m')

                        if esc == 'b':
                            print(' Você desfere um soco perfeito em direção a cabeça do cacique, mas antes que o golpe acerte,'), time.sleep(2)
                            print('\033[31m'), print('o cacique acerta um chute bem nas suas costelas (parece que alguns ossos se quebraram) você não tem mais forças para se mover.'), print('\033[m')

                    if esc == 'c':
                        print(emoji.emojize(':bust_in_silhouette: - Você teve bons reflexos para esquivar do ataque  [ VIDA: 3/3 ]')), time.sleep(1)
                        print(emoji.emojize(' O cacique viu que você é um daqueles que fica correndo da luta e se estressa :rage: desferindo varios golpes rápidos:',variant='emoji_type', use_aliases=True))
                        print('a) Esquivar'), time.sleep(0.4)
                        print('b) Revidar com golpes e defesa')
                        esc = str(input('- '))
                        if esc == 'b':
                            print(emoji.emojize('Um duelo intenso foi travado, chutes, socos :punch:, bloqueios :no_good:',variant='emoji_type', use_aliases=True))
                            playsound('songs/Fight.mp3')
                            print('porém o cacique é mais forte e seus ataques e defesas são menos efetivos do que os do cacique'), time.sleep(2)
                            print('Vocês dois ficam exaustos, mas dentre toda a poeira levantada pela intensa batalha...'), time.sleep(2)
                            print('\033[31m'), print(emoji.emojize('é você... quem está caido no chão :skull:[ VIDA: 0/3 ]',variant='emoji_type', use_aliases=True)), print('\033[m')

                        if esc == 'a':
                            print(emoji.emojize(' Você fica um pouco cansado, mas consegue desviar de todos os golpes rapidos do cacique')), time.sleep(2)
                            print(emoji.emojize('Cacique fica muito furioso :rage: e usa todas as suas energias em um super chute aéreo,',variant='emoji_type', use_aliases=True)), time.sleep(2)
                            print('ele escala em uma árvore para pegar distância e salta em sua direção'), time.sleep(1)
                            print('a) Defender'), time.sleep(0.4)
                            print('b) Esquivar')
                            esc = str(input('- '))
                            if esc == 'a':
                                print('\033[31m'), print('Você vai confiante defender do super ataque do cacique, porém com a altura o golpe se torna tão poderoso que até o chão estremece,'), time.sleep(2)
                                print('o cacique cai em cima de você com seu chute aéreo, você é completamente esmagado. [ VIDA: 0/3 ]'), print('\033[m')
                            if esc == 'b':
                                print('Cacique pula da arvore em sua direção, ele cai, levantando a terra do chão, mas você consegue desviar custando-lhe alguns arranhões.'), time.sleep(2)
                                print('O cacique está exausto e ao mesmo tempo grita, pois torceu o tornozelo. Você ve uma chance de acabar com esse duelo.')
                                print('a) gancho')
                                input('- ')

                                print('Você ve que o cacique não consegue mais se mover, e desfere um gancho perfeito'), time.sleep(2)
                                print('bem no queixo do cacique, ele cai no chão inconsciente.'), time.sleep(1)
                                print('Toda a aldeia se surpreende, porém foi uma batalha justa'), time.sleep(1)
                                print('Você se torna o novo Cacique da aldeia.'), time.sleep(1)
                                print('\033[34m')
                                print('O sinal de SOS que você tinha feito teve efeito e um navio cargueiro que estava passando por perto, viu o sinal de Socorro e foi em direção da ilha, '), time.sleep(3)
                                print('Você acaba de se tornar Cacique de uma tribo, mas pode voltar para casa... Então, qual será sua proxima decisão?'), time.sleep(2)
                                print('\033[m')
                                fim(nome)
                                print('\033[36m')
                                print(emoji.emojize(':checkered_flag: Welcome to the Island :checkered_flag:',variant='emoji_type', use_aliases=True))
                                print('\033[m')
                                playsound('songs/Vitoria.mp3')
                             ############################

                if esc == 'c':
                    print(emoji.emojize(':bust_in_silhouette: - O cacique vem em sua direção com uma cara de poucos amigos pra conversar sobre quem você é e de onde você veio')), time.sleep(2)
                    print('Você ve que está em minoria e decide agir conscientemente implorando pela sua vida e fazendo o que eles quiserem que você faça'), time.sleep(2)
                    print('\033[31m'), print('Você vive como escravo, trabalhando pelos interesse do cacique e da aldeia '), print('\033[m')
else:
    print('\033[31m'), print('Comando Inválido'), print('\033[m')