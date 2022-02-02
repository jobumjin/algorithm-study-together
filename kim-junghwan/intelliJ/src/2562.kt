/*9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.

예를 들어, 서로 다른 9개의 자연수

3, 29, 38, 12, 57, 74, 40, 85, 61

이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.*/

/*fun main(){
    var max=0
    var count=0
    for(i in 1 until 9)
    {
        var num:Int= readLine()!!.toInt()

        if(max<num){
            max=num
           count=i
        }

    }
    println(max)
    println(count)



}*/

fun main(args: Array<String>){

    var maxNum = 0
    var maxLine = 0

    for (i in 0 until 9) {
        val inputNum:Int = readLine()!!.toInt()

        if (maxNum < inputNum) {
            maxNum = inputNum
            maxLine = i
        }
    }

    println("$maxNum\n${maxLine + 1}")
}
