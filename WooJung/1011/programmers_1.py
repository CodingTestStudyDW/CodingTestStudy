def solution(record):
    person = []
    start = []
    answer = []
    dict = {}
    for string in record:
        a = string.split(" ")
        if a[0] == "Enter":
            person.append(a[1])
            start.append('Enter')
            dict[a[1]] = a[2]
        elif a[0] == "Leave":
            person.append(a[1])
            start.append('Leave')
        else:
            dict[a[1]] = a[2]
    for i in range(len(person)):
        if start[i] == "Enter":
            name  = dict[person[i]]
            sent = f'{name}님이 들어왔습니다.'
            answer.append(sent)
        else:
            name = dict[person[i]]
            sent = f'{name}님이 나갔습니다.'
            answer.append(sent)

    return answer


  
################################################

def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    
    # name 대로 dictionary에 저장하기 위함
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]
    
    #change할때 빼고 answer에 append
    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
