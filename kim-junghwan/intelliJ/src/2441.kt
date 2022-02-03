fun main(){
    val num:Int= readLine()!!.toInt()
    for(i in 1 .. num){

        for(z in 1 until i){
            print(" ")
        }
        for(j in i..num)
        {
            print("*")
        }
        println()

    }

}