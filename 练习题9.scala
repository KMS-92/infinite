/**
  * Created by 虞姬1987 on 2018/7/26.
  */
object temp{
  def main(args:Array[String]){
    var wendu=List(20,25,30,35,40,25)
    var b=4
    for (i<-Range(0,5)){
      if(i == 2){
        println("周三"+"温度："+wendu(i))
      }else{
        println(wendu(i))
      }
    }
  }
}
