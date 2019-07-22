import backend as b

doc1="Su yerken boğuldum."
doc2="Su uyur düşman uyumaz."

b.import_contents(doc1)
b.import_contents(doc2)

v1=b.func.doc2vec(doc1)
v2=b.func.doc2vec(doc2)

print(b.func.cossim(v1,v2))
