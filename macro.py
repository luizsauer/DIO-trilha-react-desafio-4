##### Imperial Age Shard #####
##### AUTO FOLLOW COM FIREBALL #####
### Me deve trazer mais 8 jogadores pro shard ###

# CONFIG
maxDist = 10
followTarget = 0x15798  # Substitua pelo serial do jogador a ser seguido
attackedNPCs = set()
currentlyFollowing = False

SetQuietMode(True)


def FollowPlayer():
    global currentlyFollowing

    if followTarget and FindObject(followTarget):
        dist = Distance(followTarget)

        if dist > 1:
            if not currentlyFollowing:
                HeadMsg("Seguindo " + Name(followTarget), 'self', 39)
                currentlyFollowing = True
            Follow(followTarget)
        else:
            if currentlyFollowing:
                HeadMsg("Perto de " + Name(followTarget), 'self', 39)
                currentlyFollowing = False
    else:
        HeadMsg("Alvo inválido ou fora do alcance.", 'self', 33)
        currentlyFollowing = False


def AttackEnemies():
    global attackedNPCs

    # Busca um inimigo válido (Murderer ou Criminal) próximo
    if GetEnemy(['Murderer', 'Criminal'], 'Any', 'Closest', 'Any', maxDist):
        enemy = GetAlias('enemy')

        # Se o inimigo for válido e estiver ao alcance, ataca
        if enemy and Distance(enemy) <= maxDist and not Dead(enemy):
            if enemy not in attackedNPCs:
                Cast('Fireball', enemy)  # Lança a magia! Se quiser alterar, basta mudar o nome da magia
                WaitForTarget(2000)
                Target(enemy)
                attackedNPCs.add(enemy)  # Marca o inimigo como atacado para não atacar novamente
        else:
            # Remove inimigos inválidos da lista e cancela o alvo
            if enemy in attackedNPCs:
                attackedNPCs.remove(enemy)
            CancelTarget()
    else:
        # Se nenhum inimigo foi encontrado, cancela qualquer target ativo
        CancelTarget()

    # Limpar NPCs mortos da lista para evitar falha no código!
    for npc in list(attackedNPCs):
        if Dead(npc):
            attackedNPCs.remove(npc)


# MAIN
if followTarget == 0x000000:
    HeadMsg("ERRO: Defina um serial válido para seguir!", 'self', 33)
else:
    while True:
        FollowPlayer()
        AttackEnemies()
        Pause(500)
        
        





##### Imperial Age Shard #####
##### AUTO ATTACK + AUTO HEAL + AUTO PET HEAL #####
### ME DEVE MAIS 3 JOGADORES PRO IMPERIAL ###

SetQuietMode(True)

# CONFIGURAÇÕES
maxDist = 10  # Distância máxima para atacar NPCs
pet = None  # Pet selecionado para curar ! Apenas variável, nao alterar manualmente.

# SELEÇÃO DO PET
SysMessage("Selecione o pet para curar ou aperte ESC para cancelar.", 84)
PromptMacroAlias('pet')
pet = GetAlias('pet')

if pet:
    HeadMsg("Pet selecionado: " + Name(pet), 'self', 64)
else:
    SysMessage("Nenhum pet selecionado!", 39)


# FUNÇÃO: Ataca qualquer NPC Murderer ou Criminal
def AttackEnemies():
    if GetEnemy(['Murderer', 'Criminal'], 'Any', 'Closest', 'Any', maxDist):
        enemy = GetAlias('enemy')
        if enemy and not Dead(enemy):
            Attack(enemy)


# FUNÇÃO: Auto cura do jogador
def HealSelf():
    if not Dead() and Hits() < MaxHits() - 10 and not BuffExists("Healing") and FindType(0xe21, -1, 'backpack'):
        BandageSelf()


# FUNÇÃO: Auto cura do pet selecionado
def HealPet():
    if pet and FindObject(pet) and Distance(pet) < 2 and Hits(pet) < MaxHits(pet) and not BuffExists("Healing"):
        if FindType(0xe21, -1, 'backpack'):
            UseObject('found')
            WaitForTarget(1000)
            if TargetExists():
                Target(pet)


# LOOP PRINCIPAL
while True:
    AttackEnemies()
    HealSelf()
    HealPet()
    Pause(500)  # Pequena pausa para evitar spam de comandos