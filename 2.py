import os
import json
print(os.getcwd())

# print(os.path.join("CodePTIT"))
dir=os.getcwd()
i=0
# for files in os.listdir('CodePTIT'):
#     file_path=os.path.join('CodePTIT',files)
#     with open(file_path,'r') as file:
#         for line in file:
#             print(line,i,end=" ")
#             print()
#             i+=1

with open("questions_answers.json",'r') as file:
    content=json.load(file)
    print(content[1]['question'])