import java.lang.Math.sqrt
import java.util.*
import kotlin.math.sqrt

fun main(args:Array<String>){
        print("Enter cofficients")
    var sc = Scanner(System.`in`)
    var a = sc.nextInt()
    var a1 = a.toFloat()
    var b = sc.nextInt()
    var b1 = b.toFloat()
    var c = sc.nextInt()
    var c1 = c.toFloat()
    var d = (b*b)-4*a*c
    var m=d.toFloat()

    print(d)
    if (d < 0 ){

        var fin = d/-1
        var res=fin.toFloat()
        var value = sqrt(res)
        var real = -b1/(2*a)
        var img = value/(2*a)
        print("\n Root is: ${real}+${img}i")

    }
    else {
    var result = sqrt(m)
        var root1 = (-b+result)/(2*a)
        var root2= (-b-result)/(2*a)
        print("\nroot1:${root1}\n"+"root2:${root2}")

    }


}




