function solution(number, limit, power) {
    var answer = 0;
    numList = []
    for (var i = 1; i <= number; i++ ){
        numList.push(solve(i))
    }
    console.log(numList)

    for(var i = 0; i < number; i++){
        if(numList[i]<=limit){
            answer += numList[i]
        }
        else{
            answer += power
        }

    }
    return answer;
}

function solve(number){
    count = 0
    for (var i =1; i <= Math.sqrt(number); i++){
        if(number % i == 0){
            count++
            if(number / i != i){
                count ++
            }
        }
    }

    return count
}

console.log(solution(5,3,2))
console.log(solution(10,3,2))