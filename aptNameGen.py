# aptNameGen
# Created by Evildaemond - DEC 2017
# Forked by PoxyDoxy because memes
# Ever wanted to make a Advanced Persistant Threat Group or Some Cyber Crew and cant come up with that perfect name
# Well, This product is just for you, with our advanced lists, we can randomly generate you a new crew name without spendig days ripping your hair out
# Its not just for the groups either, wanted to attribute to somebody but dont want to call them'just another threat actor", well now you can come up with one on the spot.
# I am sorry this is in python, please forgive me

names_to_generate = 100

from random import *

wordList = ['Bear','Red','Equation','Unknown','Cyber','Drill','Lazarus','Shadow','Dark','North','Global','Honk','Cone','Fan','Mango','Hacker','Nether','Abyss','Odyssey','Limit','Spicy','Black','Fate','Crank','Dragon','Space','Lag']
collectiveNames = ['Group','Collective','Crew','Krew','Confederate','Union','Brokers','Organisation','Crowd','Faction','Cluster','Team','Company','Conglomerate','Consolidation','Gang','Legion','Security','Army','Front']
defineList = ['anti','the','cyber','secure','cult','revolution','global','our','agent','phantom','psycho','stealth','liberation']
randomWord = ['Mantis','Bear','Hell','Project','Seven','Six','Nine','Doom','Pawn','Net','Cyber','Blade','Hacker','Hawk','Cicada','Gear','Wolf','Barron','Lords','Phreaks','Prime','Crypto']
boringLetters = ['YDT','JGG','NHK','AIE','HLS','UBD','KPR','PUJ','ZPH','EXM','RLN','SWV','QZZ','SPZ','IED','LZV','LUI','CSG','OND','XUF','JFK','CBR','PER','BRS','MEL','DAR','PHL']
portNumbers = ['7','11','13','15','17','19','21','22','23','25','26','37','49','53','67','69','70','79','80','81','82','83','84','88','102','110','111','119','123','129','137','143','161','175','179','195','311','389','443','444','445','465','500','502','503','515','520','523','554','587','623','626','631','636','666','771','789','873','902','992','993','995','1010','1023','1025','1099','1177','1200','1234','1311','1434','1471','1604','1723','1777','1883','1900','1911','1962','1991','2000','2067','2082','2083','2086','2087','2123','2152','2181','2222','2323','2332','2375','2376','2404','2455','2480','2628','3000','3128','3306','3386','3388','3389','3460','3541','3542','3689','3749','3780','3784','3790','4000','4022','4040','4063','4064','4070','4369','4443','4444','4500','4567','4800','4848','4911','4949','5000','5001','5006','5007','5008','5009','5060','5094','5222','5269','5353','5357','5432','5555','5560','5577','5632','5672','5683','5900','5901','5984','5985','5986','6000','6379','6664','6666','6667','6881','6969','7071','7218','7474','7547','7548','7657','7777','7779','8000','8010','8060','8069','8080','8081','8086','8087','8089','8090','8098','8099','8112','8139','8140','8181','8333','8334','8443','8554','8649','8834','8880','8888','8889','9000','9001','9002','9051','9080','9100','9151','9160','9191','9200','9418','9443','9595','9600','9943','9944','9981','9999','10000','10001','10243','11211','12345','13579','14147','16010','17000','18245','20000','20547','21025','21379','23023','23424','25105','25565','27015','27017','28017','30718','32400','32764','37777','44818','47808','48899','49152','49153','50070','50100','51106','55553','55554','62078','64738']
cleanup = [",","'","[","]"," "]

runs = names_to_generate
run = 0
last_group = 0

def wordgen():
	# Return Leet Word for Leat Name, so L33t
	global last_group
	global cleanup
	group = randint(1, 6)
	# Prevent Double Matching Groups
	while group == last_group:
		group = randint(1, 6)
	last_group = group

	word = ""
	if group == 1:
		word = sample(wordList, 1)
	if group == 2:
		word = sample(collectiveNames, 1)
	if group == 3:
		word = sample(defineList, 1)
	if group == 4:
		word = sample(randomWord, 1)
	if group == 5:
		word = sample(boringLetters, 1)
	if group == 6:
		word = sample(portNumbers, 1)
	word = str(word)
	for dirt in cleanup:
		word = word.replace(dirt, "")
	return word

def namegen():
	# Return New Leet Random Goodness
	return str(wordgen()) + str(wordgen())

while run < runs:
	print("Your new L33t Name is: %s" % namegen())
	run = run + 1