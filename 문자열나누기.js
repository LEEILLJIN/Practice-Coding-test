function solution(s) {
    var answer = 0;
    var testdict = {}
    var testdict2= {"first":"", "second":0}
    testdict2["first"] = s[0]
    for (var i = 0; i < s.length; i++){
        testdict[s[i]] = 0
    }
    testdict[testdict2["first"]]++
    for (var i = 1; i < s.length; i++){
        if(testdict2["first"] == s[i]){
            testdict[s[i]]++
        }else{
            testdict2["second"]++
        }

        if(testdict[testdict2["first"]] == testdict2["second"]){
            testdict2["second"] = 0
            testdict[testdict2["first"]] = 0
            testdict2["first"] = s[i+1]
            answer++
        }
    }
    if(testdict2["first"] != undefined){
        answer++
    }
    return answer;
}

console.log(solution("banana"))
console.log(solution("abracadabra"))
console.log(solution("aaabbaccccabba"))
console.log(solution("aaabcdaa"))



//aaabcdaa
//aaabcd aaaaaaaaa
// ba na na 
//abracadabra
// ab ra ca da br a
//X 1
//aaabbacc ccab ba