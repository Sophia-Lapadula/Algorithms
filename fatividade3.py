def back(p,k):
    if(sum(p)==(-1)*len(p)):
        if(minimo>k or minimo ==-1):
            minimo=k
    else:
        k+=1
        realCand=[k]
        a=[-10,-17,-6,-15,10,17,15,6]
        for i in range(len(a)):
            if isCandidate(jogo['cavalo'],a[i],p)==True:
                realCand.append(a[i])
        for i in range(len(realCand)):
            ant=jogo['peao'][i]
            H=jogo['cavalo']
            H=H+realCand[i]
            for j in range(len(jogo['peao'])):
                if(H==jogo['peao'][j]):
                    jogo['peao'][j]=-1
                if(jogo['peao'][i]!=-1) or (at>56 and at<64):
                    jogo['peao'][i]+=8

                at=jogo['peao'][i]
                if(at>56 and at<64):
                    if(ant!=at):
                        back(p,k)
