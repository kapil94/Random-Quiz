import random,os

question_path='/home/kapil/Desktop/Random_Quiz/Random_quiz/Question_papers'  # Path at which question papers will be created
answer_path='/home/kapil/Desktop/Random_Quiz/Random_quiz/Answer_keys'	# Path at which Answer papers will be created


answer_key={

		"Alabama":"Montgomery","Alaska":"Juneau","Arizona":"Phoenix","Arkansas":"Little Rock","California":"Sacramento",
	        "Colorado":"Denver","Connecticut":"Hartford","Delaware":"Dover","Florida":"Tallahassee","Georgia":"Atlanta",
	        "Hawaii":"Honolulu","Idaho":"Boise","Illinois":"Springfield","Indiana":"Indianapolis","Iowa":"Des Moines",
	        "Kansas":"Topeka","Kentucky":"Frankfort","Louisiana":"Baton Rouge","Maine":"Augusta","Maryland":"Annapolis",
	        "Massachusetts":"Boston","Michigan":"Lansing","Minnesota":"Saint Paul","Mississippi":"Jackson","Missouri":"Jefferson City",
	        "Montana":"Helena","Nebraska":"Lincoln","Nevada":"Carson City","New Hampshire":"Concord","New Jersey":"Trenton",
	        "New Mexico":"Santa Fe","New York":"Albany","North Carolina":"Raleigh","North Dakota":"Bismarck","Ohio":"Columbus",
	        "Oklahoma":"Oklahoma City","Oregon":"Salem","Pennsylvania":"Harrisburg","Rhode Island":"Providence",
	        "South Carolina":"Columbia","South Dakota":"	Pierre","Tennessee":"Nashville","Texas":"Austin",
	    	"Utah":"Salt Lake City","Vermont":"Montpelier","Virginia":"Richmond","Washington":"Olympia",
	    	"West Virginia":"Charleston","Wisconsin":"Madison","Wyoming":"Cheyenne"
	}
	
	
question_paper=[
		"Exam paper1","Exam paper2","Exam paper3","Exam paper4","Exam paper5"
		"Exam paper6","Exam paper7","Exam paper8","Exam paper9","Exam paper10",
		"Exam paper11","Exam paper12","Exam paper13","Exam paper14","Exam paper15",
		"Exam paper16","Exam paper17","Exam paper18","Exam paper19","Exam paper20",
		"Exam paper21","Exam paper22","Exam paper23","Exam paper24","Exam paper25",
		"Exam paper26","Exam paper27","Exam paper28","Exam paper29","Exam paper30",
		"Exam paper31","Exam paper32","Exam paper33","Exam paper34","Exam paper35"


		]
answer_paper=[

		"Answer key1","Answer key2","Answer key3","Answer key4","Answer key5",
		"Answer key6","Answer key7","Answer key8","Answer key9","Answer key10",
		"Answer key11","Answer key12","Answer key13","Answer key14","Answer key15",
		"Answer key16","Answer key17","Answer key18","Answer key19","Answer key20",
		"Answer key21","Answer key22","Answer key23","Answer key24","Answer key25",
		"Answer key26","Answer key27","Answer key28","Answer key29","Answer key30",
		"Answer key31","Answer key32","Answer key33","Answer key34","Answer key35"




		]


		
def Storing_quest_answer():
	global answer_key
	li=[]
	for i in range(0,34):
		li=list(answer_key.items())
		random.shuffle(li)
		answer_key=dict(li)
			
		for key in answer_key.keys():
			storing_questions(key,question_paper[i])
			storing_answers(answer_key[key],answer_paper[i])
		 		


def storing_answers(key,value):
	
	answer_obj=open(os.path.join(answer_path,value),'a')
	answer_obj.write(key+'\n')
	answer_obj.close()
	
def storing_questions(key,value):
	
	question_obj=open(os.path.join(question_path,value),'a')
	question_obj.write("The Capital of State of "+key+" is ?"+'\n')
	question_obj.close()
		





Storing_quest_answer()
