from collections import deque

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    doc_idx = deque()
    doc = deque()


    for i in range(N):      #프린트 할 문서의 중요도를 인덱스와 함께 넣기
        doc_idx.append(i)
        doc.append(data[i])
    # print(doc_idx, doc)


    count = 0
    while doc:  #doc안에 찾는 문서가 없어질 때까지
        if doc[0] == max(doc):
            count += 1
            if doc_idx[0] == M:
                print(count)
                break
            else:
                doc_idx.popleft()
                doc.popleft()
        else:
            doc_idx.append(doc_idx.popleft())
            doc.append(doc.popleft())