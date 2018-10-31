function Todo(thing,time){
    this.thing=thing;
    this.time=time;
}
var todo1=new Todo("给老婆打电话","9：00");
var todo2=new Todo("下班去市场买菜","12：00");
var todo3=new Todo("上班","14：00");
var mylist=[todo1,todo2,todo3];
console.log(todo1);
//添加事件,参数用于添加在label标签
function add(labelText){
     //添加li标签
     var para=document.createElement("li");
       var element=document.getElementById("listul");
       element.appendChild(para);

       //往新的li标签添加复选框
       var inp=document.createElement("input");
       inp.type="checkbox";
       inp.onclick = isAll;

       element.lastChild.appendChild(inp);

       //往新的li标签添加label
       var lb=document.createElement("label");
       lb.appendChild(document.createTextNode(labelText));
       element.lastChild.appendChild(lb);

       //往新的li标签添加删除按钮
       var butt=document.createElement("button");
       butt.appendChild(document.createTextNode("删除"));
        element.lastChild.appendChild(butt);
       butt.onclick=function(){
          butt.parentNode.parentNode.removeChild(butt.parentNode);
       };
}
//初始化todolist
function initList(){
    console.log(mylist.length);
    for(var i=0;i<mylist.length;i++){
       add(mylist[i].time+mylist[i].thing);
   }

}

//添加
function addListDo(){
    var labelText=document.getElementById("thing").value;

    if(labelText==""||labelText==null)return;
    else{
        //调用添加函数
     add(labelText);
       //将输入框重置
    document.getElementById("thing").value="";
    }

    }

    function getKey()
{
    if(event.keyCode===13){
    addListDo();
    }
}

//删除全部
function delectAll(){
    var listul=document.getElementById("listul");
    listul.innerHTML="";
}

//选择全部的复选框onclick响应事件
function select_cancelAll(){
     var sel=document.getElementById("selectall");

     if(sel.checked){
          var item=document.getElementById("listul");
          var items=item.getElementsByTagName("input");
         for(var i=0;i<items.length;i++){
             items[i].checked=true;
         }
     }
     else{
          var item=document.getElementById("listul");
          var items=item.getElementsByTagName("input");
         for(var i=0;i<items.length;i++){
             items[i].checked=false;
     }
 }
}

//是否全部被选中
function isAll(){
  var sel=document.getElementById("selectall");
    if(this.checked==false){
      sel.checked = false;
      return;
    }
  else{
var item=document.getElementById("listul");
var items=item.getElementsByTagName("input");

    for(var i=0;i<items.length;i++){
           if(items[i].checked==false){
             return;
           }
      }
    sel.checked = true;
  }
}