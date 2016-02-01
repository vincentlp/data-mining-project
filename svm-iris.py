from sklearn import svm
from sklearn import datasets
from sklearn.cross_validation import KFold
clf = svm.SVC()

#par defaut gaussien et si on veut polynome degre k on modifie par clf = svm.SVC(kernel="poly",degree=2)

iris = datasets.load_iris()
X, y = iris.data, iris.target



#on va creer les ensmbles de tests
#avec python X=X[ind] si ind est un nombre on veut celui dont l'indice est ind et si on met un tableau on reindexe ce tableau

from random import shuffle
from random import seed

ind = [i for i in range(150)]
#on melange les index de maniere aleatoire selon la graine 15
shuffle(ind, seed(15))
#on remplace X par sa nouvelle indexation
X=X[ind]
y=y[ind]

#3 0 en flottants car 3 types d'iris
pre=[0.0,0.0,0.0]
rap=[0.0,0.0,0.0]

#on rajoute la partie validation croisee grace a KFold
kf = KFold(150, n_folds=10)
for train,test in kf:

#on prend les 100 premieres valeurs, 100 exclu
    train_X=X[train]
#de 100 jusqu'a la fin
    test_X=X[test]
#on prend les 100 premieres valeurs, 100 exclu
    train_y=y[train]
#de 100 jusqu'a la fin correspond a "p" plus loin
    test_y=y[test]

    clf.fit(train_X,train_y)

    p = list(clf.predict(test_X))
# print p

#Precision et rappel:
# precision= nb indiv correctement predits en classe i / nb indiv predits en classe i
# rappel = nb indiv correctement predits en classe i / nb indiv en classe i

#donne un tableau de booleens donc on doit sommer car pour tous les 1 c'est vrai
    for c in range(3):
        if sum([p[i]==c for i in range(len(test_y))])>0:
            pre[c] += float(sum([p[i]==test_y[i] for i in range(len(test_y)) if test_y[i]==c]))/float(sum([p[i]==c for i in range(len(test_y))]))
#on fait pareil pour le rappel
        if sum([test_y[i]==c for i in range(len(test_y))])>0:
#pour si jamais denominateur est nul on met >0
            rap[c] += float(sum([p[i]==test_y[i] for i in range(len(test_y)) if test_y[i]==c]))/float(sum([test_y[i]==c for i in range(len(test_y))]))

#on a ajoute dans les trois cases du tableau a chaque fois qu'on est passe par la boucle donc on doit diviser par 10
for p in range(3):   
    print "Precision moyenne classe "+str(p) + ": "+str(pre[p]/10.)
    print "Rappel moyen classe "+str(p) + ": "+str(rap[p]/10.)



