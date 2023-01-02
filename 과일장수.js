function solution(k, m, score) {
    //score를 m개로 쪼갠 후 각 상자의 최소 점수 * m의 누적합의 최대
    var answer = 0;
    const sortedScore = score.sort()
    const reversedScore = sortedScore.reverse()
    console.log(reversedScore)
    temparray = []
    if(score.length < m){
        return answer
    }else{
        for(var i = 0; i < score.length; i++){
            console.log(i)

            // if((score.length - (i)) >= m){
                if(temparray.length <= m){
                    temparray.push(score[i])
                    console.log(temparray)
                }
            // }else{
            //     break
            // }

            if(temparray.length == m){
                answer += Math.min(...temparray) * m
                temparray = []
            }

        }
    }
    return answer;
}

console.log(solution(3,4,[1, 2, 3, 1, 2, 3, 1]))
console.log(solution(4,3,[4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]))