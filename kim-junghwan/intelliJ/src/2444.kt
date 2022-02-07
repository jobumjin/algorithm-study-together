fun main(){
    val num:Int= readLine()!!.toInt()

    for(i in 0 until num )
    {
        for(j in i until num-1)
        {
            print(" ")
        }
        for(j in 0 until 2.times(i+1).minus(1) )
        {
            print("*")
        }
        println()
    }

    for(i in num downTo 1)
    {
        for(j in i until num.plus(1))
        {
            print(" ")
        }
        for(j in 0 until (i-1).times(2).minus(1))
        {
            print("*")
        }
        println()
    }

}