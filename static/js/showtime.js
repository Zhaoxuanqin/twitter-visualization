// 放一个显示时间的小模块
var t = null;
// 这个定时器有啥用呀？？？
t = setTimeout(time,1000);//開始运行，是不会每1000ms运行一次time函数？
function time()
{
    clearTimeout(t);//清除定时器
    dt = new Date();
    var show_day=new Array('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    var y   = dt.getFullYear();
    var mt  = dt.getMonth()+1;
    var day = dt.getDate();
    var week = dt.getDay();
    var h   = dt.getHours();//获取时
    var m   = dt.getMinutes();//获取分
    var s   = dt.getSeconds();//获取秒
    document.getElementById("showTime").innerHTML = show_day[week-1]+" "+ y+"-"+mt+"-"+day+"/"+h+":"+m+":"+s;

    t = setTimeout(time,1000); //设定定时器，循环运行
}