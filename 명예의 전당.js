function solution(k, score) {
    var answer = [];
    var honorList = [];
    const day = score.length;
    honorList.push(score[0]);
    answer.push(score[0]);

    for(var i = 1; i < day; i++){
        if(honorList.length < k){
            honorList.push(score[i])
            answer.push(Math.min(...honorList))
            console.log("honorList.length <= k",honorList)

        }else{
            if(score[i] > Math.min(...honorList)){
                console.log(score[i])
                console.log("(score[i] > Math.min(...honorList)",honorList)
                temp = honorList.findIndex((e) => e == Math.min(...honorList))
                console.log(honorList.indexOf(Math.min(...honorList)))
                console.log("honorList.filter",honorList)
                honorList.splice(temp,1)
                honorList.push(score[i])
                console.log("push(score[i])", honorList)
                answer.push(Math.min(...honorList))
            }else{
                answer.push(Math.min(...honorList))
            }
        }
        // for(var j = 0; j < ; j++){
        //     if(honorList.length <= k)
        //     honorList.push(score[i])
        // }
    }
    return answer;
}

console.log(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))