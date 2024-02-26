from rank_bm25 import BM250kapi
corpus=["Nguyễn Hải Lâm","Hải Lâm"]
token=[doc.split() for doc in corpus]
print(token)
bm25=BM250kapi(token)
print(bm25)