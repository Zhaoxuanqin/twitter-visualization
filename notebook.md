big_screen项目学习笔记

发布博客的时候，改名为：

用flask+echarts打造一个数据可视化的大屏幕

# 1. 项目说明

源自github上逛到的一个项目，用flask和echarts实现了一个大屏幕显示，运行app.py后，在网页上输入如下url地址就能看到效果，如图。

![image-20201014172132837](big_screen项目学习笔记.assets/image-20201014172132837.png)

经过自己的研究分析，发现网页最底下一层是一个蓝色的背景，带有一个跟随鼠标的粒子动态特效，接着在这个上面叠加了一个table。

table的布局如下所示，首先是一个标题，标题的右侧是天气和时间。接着是分为三列，左侧三列显示3个图表，中间一列显示两个类似数字时钟的数据和文字说明，右边一列显示3个图表。其中左下角的图表由3个小的图表组合而成。

![image-20201014172655464](big_screen项目学习笔记.assets/image-20201014172655464.png)

# 2. 项目文件布局

项目主要由4个部分组成，data部分是数据准备，app部分是flask服务，templates部分控制网页的显示，这三者正好对应MVC的设计模式。最后的static里面主要保存一些网页元素，例如字体格式、图片等等，以及必要的一些js函数库。下面就这四个部分做一个简要的注释。

![image-20201014171821416](big_screen项目学习笔记.assets/image-20201014171821416.png)

# 3. 四大模块核心代码分析

## 3.1 数据准备模块

这里有3个数据，以data.py为例，文件中，定义了一个数据类，初始化的时候产生详细的数据，然后定了一个函数返回格式化的数据。

图表的数据用json格式保存，在返回给pyecharts的时候用get函数组装成数组的形式。

```python
class SourceDataDemo:
    
	def __init__(self):
        # 整个网页的标题
        self.title = '大数据可视化展板通用模板'
        # 总共是6个图表，数据格式用json字符串，这是第1个图标的数据
        self.echart1_data = {
            'title': '行业分布',
            'data': [
                {"name": "商超门店", "value": 47},
                {"name": "教育培训", "value": 52},
                {"name": "房地产", "value": 90},
                {"name": "生活服务", "value": 84},
                {"name": "汽车销售", "value": 99},
                {"name": "旅游酒店", "value": 37},
                {"name": "五金建材", "value": 2},]}
        
    @property
    def echart1(self):
        data = self.echart1_data
        echart = {
            'title': data.get('title'),
            # 第一次get获取到的是许多键值对，所以需要对每个键值对再次get
            'xAxis': [i.get("name") for i in data.get('data')],
            'series': [i.get("value") for i in data.get('data')]
        }
        # 返回的是标题和对应的数据，并没有说用什么方式展现！
        return echart
```

## 3.2 flask网页服务模块

准备好了数据之后，就可以把数据放到html中调用pyecharts进行渲染，这里使用flask服务，将URL根目录和index.html绑定。

```python
# 新建一个flask服务
app = Flask(__name__)

# 建立一个URL连接
@app.route('/')
def index():
    # 新建一个实例
    data = SourceData()
    # 在这里传入数据，发送给index进行渲染
    return render_template('index.html', form=data, title=data.title)

# 运行flask
if __name__ == "__main__":
    app.run(host='127.0.0.1', debug=False)
```

## 3.3 网页视图模块

首先是jquery和css文件的加载，jquery是js的一个函数库，css决定了整个网页的字体字号颜色等风格。

然后是一个加载动画，这个加载动画使得网页加载具有淡入的效果，并且确保了网页在拉伸的时候能自适应调整布局，关于这个函数后面再详细解释。

最后是echarts的函数库和中国地图的函数库。

```html
<head>
    <meta charset="utf-8">
    <title>刘凯凯的大屏幕</title>
    <script type="text/javascript" src="../static/js/jquery.js"></script>
    <link rel="stylesheet" href="../static/css/comon0.css">
</head>
<script type="text/javascript" src="../static/js/loading.js"></script>
<script type="text/javascript" src="../static/js/echarts.min.js"></script>
<script type="text/javascript" src="../static/js/china.js"></script>
```

接下来加载网页的背景，是一个有动态粒子的效果，粒子效果如图所示

```html
<!--这是一个动态的粒子效果图，设置了透明度为0.2-->
<div class="canvas" style="opacity: 0.9">
    <iframe frameborder="0" src="../static/js/index.html" style="width: 100%; height: 100%"></iframe>
</div>
```

![image-20201014175657966](big_screen项目学习笔记.assets/image-20201014175657966.png)

在正式页面加载进来之前，还有一个小的loading动画，配合一个gif文件和说明文字实现

```html
<!--这是一个在正式页面加载进来之前显示的加载小动画，文字可以修改-->
<div class="loading">
    <div class="loadbox"><img src="../static/picture/loading.gif"> 我正在加载中...</div>
</div>
```

![image-20201014180717197](big_screen项目学习笔记.assets/image-20201014180717197.png)

接下来就是整个网页的布局了，网页整体上是如下的一个table布局，首先是一个标题，标题的右侧是天气和时间。接着是分为三列，左侧三列显示3个图表，中间一列显示两个类似数字时钟的数据和文字说明，右边一列显示3个图表。其中左下角的图表由3个小的图表组合而成。

![image-20201014172655464](big_screen项目学习笔记.assets/image-20201014172655464.png)

### a. 网页大标题

网页大标题放在h1格式里面，然后是天气和时间显示。

天气直接加载一张图片完成，时间用一个js函数实现，每秒刷新。

```html
<div class="head">
    <h1>{{title}}</h1>
    <div class="weather">
        <img src="../static/picture/weather.png"><span>我是天气</span>
        <span id="showTime"></span>
    </div>
    <script type="text/javascript" src="../static/js/showtime.js"></script>
</div>
```

效果如图。

![image-20201014191548134](big_screen项目学习笔记.assets/image-20201014191548134.png)

### b. 左右两栏的图表

左右两侧的布局相似，左侧的第3个图表较为特殊，是3个小的环状图的组合图表。

每一列用<li>隔开，内部用<div>分隔。

```html
<li>
    <div class="boxall" style="height: 3.2rem">
        <div class="alltitle">{{form.echart1.title}}</div>
        <div class="allnav" id="echart1"></div>
        <div class="boxfoot"></div>
    </div>
    <div class="boxall" style="height: 3.2rem">
        <div class="alltitle">{{form.echart2.title}}</div>
        <div class="allnav" id="echart2"></div>
        <div class="boxfoot"></div>
    </div>
    <div class="boxall" style="height: 3.2rem">
        <div style="height:100%; width: 100%;">
            <div class="sy" id="fb1"></div>
            <div class="sy" id="fb2"></div>
            <div class="sy" id="fb3"></div>
        </div>
        <div class="boxfoot">
        </div>
    </div>
</li>
```

### c. 中间一栏的图表

中间一栏有3个部分组成，第一部分是显示数据，第二部分是显示文字，第三部分是显示一个地图。

地图包含4个图层，分别是用小地球本体，一个像魔方一样的网，一个光环，和一个中国地图。

```html
<li>
    <div class="bar">
        <div class="barbox">
            <ul class="clearfix">
                <li class="pulll_left counter">{{form.counter.value}}</li>
                <li class="pulll_left counter">{{form.counter2.value}}</li>
            </ul>
        </div>
        <div class="barbox2">
            <ul class="clearfix">
                <li class="pulll_left">{{form.counter.name}}</li>
                <li class="pulll_left">{{form.counter2.name}}</li>
            </ul>
        </div>
    </div>
    <div class="map">
        <div class="map1"><img src="../static/picture/lbx.png"></div>
        <div class="map2"><img src="../static/picture/jt.png"></div>
        <div class="map3"><img src="../static/picture/map.png"></div>
        <div class="map4" id="map_1"></div>
    </div>
</li>
```

![image-20201014192527533](big_screen项目学习笔记.assets/image-20201014192527533.png)

### d. 图表echarts属性设置

为了便于理解，这里省略了很多格式，做成类pythonic的结构。

首先是设置option，包含背景颜色、图表大小间距、坐标轴、图表类型等等，然后用option参数来配置图表样式。

```php+HTML
<script>
$(function echarts_1() {
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('echart1'));
    option = {
        backgroundColor: '#00265f',     	// 设置背景颜色这个背景颜色是不透明的
        tooltip: 							// 设置鼠标悬浮图表
            trigger: 'axis',
            axisPointer: {type: 'shadow'}},
        grid:       						// 设置图表显示范围
            left: '0%',
            top: '0%',
            right: '0%',
            bottom: '4%',
            containLabel: true   // 表示坐标轴label标签也是grid图表的一部分
        xAxis: 								// 对x轴系列选项进行设置
            type: 'category',
            data: {{form.echart1.xAxis|safe}},
            axisLine: ...
            axisTick: { show: false,},
            axisLabel:  {
                    interval: 0,
                    rotate:50,		// 坐标轴文字旋转角度
                    show: true,
                    splitNumber: 15,
                    textStyle: {
                        color: "rgba(255,255,255,.6)",
                        fontSize: '12',
					...
    	yAxis: 								// 对y轴系列选项进行设置
    		...
    	series: 							// 对具体的图表类型进行设置
       	 	type: 'bar',
            data: {{form.echart1.series|safe}},
            barWidth:'35%', //柱子宽度
            itemStyle: 
                normal: 
                    color:'#2f89cf',
                    opacity: 1,
                	barBorderRadius: 5,
		};

    // 使用刚指定的配置项和数据显示图表。
    myChart.setOption(option);
    window.addEventListener("resize",function(){myChart.resize()});
</script>
```

使用上述配置得到的图表如下，有背景颜色的区域就是grid区域

![image-20201014194116390](big_screen项目学习笔记.assets/image-20201014194116390.png)

## 3.4 static静态元素分析

static中的大部分为静态元素，例如一些图片，字体，文字样式等等。

这里的index.html和template下的index.html文件不一样，这里的文件其实是一个动态粒子的html页面，被当做半透明背景引入到正式的index文件中。这里的index.html可以单独打开，通过内嵌的js函数可以实现下图的这种效果。

![image-20201014175657966](big_screen项目学习笔记.assets/image-20201014175657966.png)

另外包含一些函数。其中有3个函数为外部应用函数，类似于python中import的类库，分别是echarts函数库，jquery函数库和中国地图china函数库。剩下的为自定义函数，一个是控制显示时间的函数，另一个是页面淡入显示和窗口自适应的函数。

### a. 显示时间的函数

设定一个定时器，每1000ms获取一次时间，然后把时间格式化成年月日时分秒的格式。

```js
var t = null;
t = setTimeout(time,1000);//開始运行，每1000ms运行一次time函数？
function time()
{
    clearTimeout(t);//清除定时器
    dt = new Date();
    var y   = dt.getFullYear();
    var mt  = dt.getMonth()+1;
    var day = dt.getDate();
    var h   = dt.getHours();//获取时
    var m   = dt.getMinutes();//获取分
    var s   = dt.getSeconds();//获取秒
    document.getElementById("showTime").innerHTML = y+"年"+mt+"月"+day+"日"+"-"+h+"时"+m+"分"+s+"秒";
    t = setTimeout(time,1000); //设定定时器，循环运行
}
```

### b. 页面淡入和视图自适应的函数

```js
//如果把这段注释掉，会一直停留在加载的页面上
$(window).load(function(){
         $(".loading").fadeOut()
        })

//这个是自适应调整窗口大小的函数，如果没有，整个页面布局会很混乱
$(document).ready(
function()
    {
        var whei=$(window).width()
        $("html").css({fontSize:whei/20})
        $(window).resize(
            function()
                {
                var whei=$(window).width()
                $("html").css({fontSize:whei/20})
                }
        );
   }
);
```

# 4. 总结

大概花了2天的时间看完这个项目，一开始看的一头雾水，仔细分析一下，其实用的都是蛮简单的技术，主要用了这三个技术

- 后端：flask
- 可视化：echarts
- 前端：HTML+JavaScript+css

后续如果继续深入研究，后端框架可以换成高性能的tornado或者功能更强大的Django，可视化的组件可以换成pyecharts，前端可以使用vue，react框架等。还可以考虑加入sqlite数据库或连接db数据库，打造成一个更完整的项目。