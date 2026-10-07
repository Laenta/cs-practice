names = ["Аня", "Боря", "Вика"]
scores = [7.0, 9.0, 9,0]
def winner(names, scores):
    best = 0
    for i in range(1, len(scores)):
        if scores[i] >scores[best]:
            best=i
    return names[best]
def average(scores):
    if len(scores)==0:
        return 0.0
    return (round(sum(scores)/len(scores),2) )
def ranking(names,scores):
    result = []
    for i in range(len(names)):
        result.append((scores[i],names[i]))
    result.sort(key=lambda x: -x[0])
    answer=[]
    for x in result:
        answer.append(x[1])
    return answer
        
def above_average(names,scores):
    avg = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i] > avg:
            result.append(names[i])
    return result
        
print(winner(names, scores))   
print (average(scores))
print(ranking(names,scores))
print(above_average(names,scores)) 

            
    