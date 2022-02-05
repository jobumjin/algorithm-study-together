fun main(){
    val num:Int= readLine()!!.toInt()

    for(i in 1 .. num){

        for(z in 1 until i )
        {
            print(" ")
        }
        for(j in 1 .. (2*num-(2*i-1)))
        {
            print("*")
        }

        println()
    }
}
