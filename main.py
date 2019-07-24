import vsm

doc1="Su yerken boğuldum düşmanlık."
doc2="Susuz uyur düşman uyumaz."
doc3="你好"
doc4="你"
vsm.import_contents(doc1,0)
vsm.import_contents(doc2,0)
vsm.import_contents(doc3,1)
vsm.import_contents(doc4,1)

v1=vsm.func.doc2vec(doc1)
v2=vsm.func.doc2vec(doc2)

v3=vsm.func.doc2vec(doc3)
v4=vsm.func.doc2vec(doc4)

print(vsm.func.cossim(v1,v2))
print(vsm.func.cossim(v3,v4))
