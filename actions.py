greatest = 0
sellPosition = 0
buyPosition = 0
actions = [7,6,4,3,1]
for position in reversed(range(len(actions))):
    curValue = actions[position]
    for position2 in range(len(actions)):
        if(curValue-actions[position2]>greatest and position2<position):
            greatest=curValue-actions[position2]
            buyPosition=position2
            sellPosition=position
if(greatest>0):
    print('Lucro das acoes '+str(greatest))
    print('Isto ocorre quando se compra no '+str(buyPosition+1) +
        ' dia da semana e se vende no '+str(sellPosition+1))
else:
    print('Nao ha nenhuma operacao que possa ser feita que de lucro.')