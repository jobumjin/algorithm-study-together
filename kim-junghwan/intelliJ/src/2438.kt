/*
* 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
*
* */

fun main()
{

    var a:Int= readLine()!!.toInt()

    for (i in 1 .. a ){
        for(j in 1.. i){
            print("*")
        }
        println()
    }




}