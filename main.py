import vsm

doc1="Su yerken boğuldum."
doc2="Su uyur düşman uyumaz."

vsm.import_contents(doc1)
vsm.import_contents(doc2)

v1=vsm.func.doc2vec(doc1)
v2=vsm.func.doc2vec(doc2)

print(vsm.func.cossim(v1,v2))
