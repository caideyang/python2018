

window.onload = function () {
    // var oTodo_Task = document.getElementById("todo-task-div");  //未完成任务的div
    var oTodo_ol = document.getElementById("todo-list");  //未完成任务列表ol
    var oNew_task = document.getElementById("new-task") ;//input添加任务项
    var oAdd_btn = document.getElementById('add-btn');
    var oTodo_count = document.getElementById("todo-count");

    oAdd_btn.onclick = function () {
        var oTodo_lis = document.getElementsByClassName("todo-task"); //未完成任务项
        var new_task = oNew_task.value.replace(/^\s+|\s+$/g,""); //对获取的任务左右去空格
        console.log(oTodo_lis.length);
        if (new_task ){
            var oTodo_li = document.createElement("li"); //创建新的任务项
            oTodo_li.className = "todo-task";
            task_id = Date.now(); //给任务添加唯一编号
            oTodo_li.id = "task_"+task_id;
            oTodo_li.innerHTML = '<input type="checkbox" onchange="update_status('+task_id+')">\n' +
                '                <span>'+new_task+'</span>\n' +
                '                <a onclick="edit_task('+task_id+')">E</a>\n' +
                '                <a onclick="del_task('+task_id+')">X</a>';
            if (oTodo_lis.length==0){
                console.log(0);
                oTodo_ol.appendChild(oTodo_li);
                // alert(oTodo_lis.length);
            //
            }else {
                // console.log(oTodo_lis[0].innerText);
                oTodo_ol.insertBefore(oTodo_li, oTodo_lis[0]);

                // alert(oTodo_lis.length);
            }
            // todo_count ++;
            oNew_task.value = ""; //清空文本内容
            oTodo_count.innerText = oTodo_lis.length;

        }else {
            alert("新增任务不能为空!");
        };

    };
};

// // 加载数据
// function load_data(task_status) {
//     //status:  undo 、finish
//     var task_data_list = document.getElementsByClassName(task_status);
//     return task_data_list;
// }
// //保存数据
// function save_data(status) {
//
// }
//
// //添加任务
// function add_task() {
//
// }
//
// //修改任务状态
// function update_status(id) {
//
// }
//
// //删除任务
// function  del_task(id) {
//
// }
//
// //编辑任务
// function edit_task(id) {
//
// }
//删除ol下的节点，修改计数
function del_node(oTask_lis, o_task_li){
    li_className = o_task_li.className;
    var o_task_lis = document.getElementsByClassName(li_className);

}
//新增ol下的节点，增加计数
function  add_node(oTask_lis, o_task_li) {

}


//修改任务状态
function update_status(id){
    var oTodo_lis = document.getElementsByClassName("todo-task"); //未完成任务项
    var oFinished_list = document.getElementsByClassName("finished-list"); //已完成任务项
    console.log(id);
    task_id = "task_" + id;
    var o_task_li = document.getElementById("task_"+id);
    // console.log(o_task_li.className);
    li_className = o_task_li.className;
        if (li_className=="todo-task"){
            o_task_li.className = "finished-task";
            del_node(oTodo_lis,task_id);
            add_node(oFinished_list,task_id);
        }else {
            li_className="todo-task";
            del_node(oFinished_list,task_id);
            add_node(oTodo_lis,task_id);
        }

    del_node(oTodo_lis, oFinished_list, o_task_li);
    add_node(oTodo_lis, oFinished_list, o_task_li);
}

//清除任务,计数清空为0
function delectAll(ol_id, count_id){
    var listul=document.getElementById(ol_id);
    var o_count = document.getElementById(count_id);
    o_count.innerText = 0;
    listul.innerHTML="";
    console.log(Date.now());

}