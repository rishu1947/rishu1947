import random


n = [' Sagar',' Harsh',' Aditya',' Nitish',' Sumit',' Anil',' Raj',' Anant',' Ajay','Aman','Krishna','Sumant','Pranav','Kabir']

p =[' Mumbai','Bhopal','Vrindawan',' Kashmir',' Indore',' Hyderabad',' Ranchi',' Kochi',' Jalandhar',' Delhi',' Punjab', 'Banglore']

t = ['took a beautiful picture','gone in celebrity meet up','day i visit my fav place','collect cans cap','studied science','played with crackers','have a lovely food']

r = ['a school student','a labour',' a streamer','a job going person','an introvert guy','a retired govt worker','master',' LPU vertos',' a mysterious guy']

we = [' a cool day',' rainy day',' cool breezy day',' a warm morning',' a bad day']

w = ['Long time back','Story goes like these','In earlier times','Once upon a time']

s = [' was known as',' named ',' known as ']

wh = [' to his colleague',' to his roomates',' to his fellow classmen', ' to his mother.',' to his father.',' to his siblings']

ne= ['After few time','2 hours later','3 years after','% eternity later']

go= [',after that he did not returned',',after his coffee he did get a cab',' ,he got mysteriously disappeared','he never returned']

sc=['.Everyone started searching','.Police case was filed','. His family was worried about him']

th=[' he somehow did a call to his family',' his father received a call from him',' he did a call to his friend rohit']

kw = [' they all went to his stated location',' they reached that location told by him']

a = [' he talked about mishappened occur with him',' he explained all that incident',' he described what happenend to him']

i = [' he told that one of his friend baited him in the name of party',' he described that how his friend has said that " let us have a party tonight',' he told whole story to his family memebers that his friend alok offered him to join tonight party']

pr = [' but his friend was involved on drug peddling',' but his friend wss a drug supplier']

ch = [' , his friend cheated him and mixed drug pills in his softdrink ',' , his friend suspiciously gave him drug pills by mixing in his drink',' ,his friend forced him consume harddrinks heavily']

addict = [' to make him get addicted of it',' so that he will get addicted to it and would spend more money on it']

prof = [' .For his own profit he betrayed his own childhood friend',' .Greedy for money he cheated his own bestfriend','.For reaching his sales target from his supplier he betrayed his own friend']

case = [' .This whole scenario was stated to the higher officials ',' .This whole scenario was stated to the police officers']

accuse = [' and they consolidated the victim that accused would not be spared', 'and they sentenced the victim that culprit would not be exempted']

new = [' .This whole news was covered on television', ' .This whole news was covered in newspaper headlines' ]

solve = [' .Later This case was solved with the help of special cops']

end = [' .From this unabridged story we can retrain that after some virtuous experiences one can also face a miserable stage ']

learnings = [' ,In addition from this narrative we can assimilate that we should never blind-trust and sometimes acquire a skeptic approach.']

randomname = random.choice(n)
randomplace = random.choice(p)
randombody = random.choice(t)
randomrole = random.choice(r)
randomweather = random.choice(we)
randomword = random.choice(w)
randomsaying = random.choice(s)
randomwhom = random.choice(wh)
randomnext = random.choice(ne)
randomgone = random.choice(go)
randomscene = random.choice(sc)
randomthen = random.choice(th)
randomknow = random.choice(kw)
randomafter = random.choice(a)
randomplot = random.choice(pr)
randomcheated = random.choice(ch)
randomprofit= random.choice(prof)
randomcase= random.choice(case)
randomaccused= random.choice(accuse)
randomnews= random.choice(new)
randomsolve= random.choice(solve)
randomend= random.choice(end)
randomlearnings= random.choice(learnings)

story = randomword + randomrole + randomsaying + randomname +' travelled a beautiful city called' +randomplace +' where it was' + randomweather + ' and in this place'  +' he' + randombody + ' after that he shared his experiences' + randomwhom + randomnext + randomgone +randomscene+randomthen + randomknow + randomafter + randomplot + randomcheated + randomprofit + randomcase + randomaccused + randomnews + randomsolve + randomend + randomlearnings
print(story)