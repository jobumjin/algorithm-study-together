fun main(){
    val num:Int= readLine()!!.toInt()

    for(i in 1.. num){

        for(z in i until  num)
        {
            print(" ")
        }
        for(j in 0 until  (2*i-1))
        {
            print("*")
        }
        println()
    }
}