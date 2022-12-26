function solution(t, p) {
    var answer = 0;
    const plength = p.length
    var NumList = []
    for (var i = 0; i < t.length; i++){

        if ((t.substr(i, plength)).length == plength){
            NumList.push(t.substr(i, plength))
        }
        
    }
    console.log(NumList)
    for (var i=0; i<NumList.length; i++){
        if(NumList[i] <= p){
            answer++
        }
    }
    return answer;
}

console.log(solution("500220839878", "7"))