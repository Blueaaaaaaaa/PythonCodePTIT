class declace:
    def __init__(self,name,birthday,score1,score2,score3):
        self.name=name
        self.birthday=birthday
        self.score1=score1
        self.score2=score2
        self.score3=score3
        self.sum=score1+score2+score3
    def output(self):
        print(self.name,self.birthday,"%.1f" %self.sum)
if __name__=="__main__":
    out=declace(input(),input(),float(input()),float(input()),float(input()))
    out.output()