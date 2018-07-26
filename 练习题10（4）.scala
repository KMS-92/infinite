import scala.collection.mutable.ListBuffer
import org.apache.spark.{SparkConf, SparkContext}
import org.json.JSONObject
import org.json.JSONObject//导入str转json工具包
import org.apache.spark.SparkConf//
/**
  * Created by 虞姬1987 on 2018/7/24.
  */
object AAAA{
  def main(args:Array[String]){
    import org.json.JSONObject//导入str转json工具包
    import org.apache.spark.SparkConf//
    import org.apache.spark.SparkContext//
    val conf = new SparkConf().setAppName("cala").setMaster("local").set("spark.testing.memory", "2147480000");
    val sc = new SparkContext(conf)//Spark运行环境,,本地电脑，集群
    sc.textFile("E:\\大数据实训\\课程作业\\江西招生人数.txt")
      .filter(line=>line.endsWith("status\":1}"))
      //          .foreach(line => println(line))
      .flatMap(line => {
      val json = new JSONObject(line)
      val jsonlist = json.getJSONArray("data")
      //        jsonlist.getJSONObject(0)
      val list = ListBuffer[JSONObject]()
      for (i <- 0 to jsonlist.length() - 1) {
        list.append(jsonlist.getJSONObject(i))
      }
      list
    }).map(line => (line.getString("school"), line.getString("plan").toInt)).reduceByKey(_ + _)
      .foreach(line => println(line))
  }
}
/**
  * 高考派 练习题10（4）
  */