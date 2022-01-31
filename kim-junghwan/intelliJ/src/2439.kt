
fun main(){
  var a:Int= readLine()!!.toInt()

    for(i in 1 .. a)
    {
        for(j in a-i downTo 1)
        {
           print(" ")

        }
        for(z in 1 .. i)
        {
            print("*")
        }
        println()
    }

}