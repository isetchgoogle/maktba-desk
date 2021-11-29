import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred=credentials.Certificate("servAccountKey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()

# creat with auto id ==> db.collection('users').add({'name':'3bouda','age':40})
# creat with known id ==> db.collection('users').document('1').set({'name':'3bouda','age':40})
# add element in doc ==>  db.collection('users').document('1').set({'adr':'tunis'},merge=True)
# get docs
def getU():
	docs =  db.collection('users').get()
	c=[]
	for doc in docs:
		c.append(doc.to_dict())
	return c

def getUId():
	docs= db.collection('users').stream()
	for doc in docs:
		print(f'{doc.id} =>{doc.to_dict()}')

def addBookFireStore():
	db.collection('users').add({  
			'CIN':'3bouda',
			'Date':40,
			'Etudiant':'dssd',
			'Livre':'dededed',
			'Référence':'zdzdzddz'
		}
	)

"""
def updateBook():
	docx= db.collection('books').where("code_X0020_livre","==",)
	docx.update({'capital':False})
	docs= db.collection('books').stream()
	for doc in docs:
		print(f'{doc.id} => {doc.to_dict()}')
"""



"""
result= db.collection('books').document().get()
if result.exists:
	print(result.to_dict())
	 print(f'{doc.id} => {doc.to_dict()}')


docs= db.collection('books').stream()
for doc in docs:
	 print(f'{doc.id} => {doc.to_dict()}')
	 
docx= db.collection('books').where("code_X0020_livre","==","Eco")	  
for doc in docx:
	   doc.id="book"
#pour ajouter a un document
docx= db.collection('books').where("code_X0020_livre","==",)
for x in docx:
	docx.id.set("bb",merge=True)

docs= db.collection('books').stream()	
for doc in docs:
	 print(f'{doc.id} => {doc.to_dict()}')
#update
docx.update({'capital':False})
docs= db.collection('books').stream()
for doc in docs:
	 print(f'{doc.id} => {doc.to_dict()}')
"""