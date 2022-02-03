/*fun main(){
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

}*/
fun main(){
    val num:Int = readLine()!!.toInt()

    if (num > 0){
        (0..num-1).forEach {
            repeat(it){
                print(" ")
            }
            repeat(num-it){
                print("*")
            }
            println()
        }
    }
}