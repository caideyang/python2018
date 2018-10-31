window.onload = load;
// localStorage存储数据结构样例：
// var task_list = [{"task_id":"12345678","task_content":"学习Python","status":false},
//                  {"task_id":"12345679","task_content":"学习Java","status":true},
//                 {"task_id":"123415678","task_content":"学习Java","status":false},
//                 {"task_id":"212345678","task_content":"做Python作业","status":true},
//                 {"task_id":"312345678","task_content":"参加考核","status":false},]
//
// var task_list = {12345678:{"task_id":"12345678","task_content":"学习Python","status":false},
//                  12345679:{"task_id":"12345679","task_content":"学习Java","status":true},
//                  123415678:{"task_id":"123415678","task_content":"学习Java","status":false},
//                  212345678:{"task_id":"212345678","task_content":"做Python作业","status":true},
//                  312345678:{"task_id":"312345678","task_content":"参加考核","status":false}}
//
// save_data("task_list", task_list);


//存储数据
function save_data(item,data) {
    data = JSON.stringify(data);
    localStorage.setItem(item,data);
    reload(); //每次保存完数据自动刷新界面
}

//获取localStorage存储的数据
function read_data(item) {
    var data = localStorage.getItem(item);
    	if(data!=null){
		return JSON.parse(data);
	}
	else return {};
}

//创建dom标签
function create_dom(father_node, task_list) {
    // var father_node = document.getElementById("todo_task_list");
    if (task_list){
        task_list.reverse();
        string = "";
        for (task in task_list){
            var task_id = task_list[task].task_id;
            var task_content = task_list[task].task_content;
            var status = task_list[task].status;
            // var o_li = document.createElement('li');
            // o_li.id = "task_" + task_id;
            string += "<li id='task_"+task_id+"'><div class='task'><input type='checkbox' onchange='update_status("+task_id+","+status+")'>\n" +
                "    <span id='span_"+ task_id + "' class='span_content' onclick='edit("+task_id+")'>"+task_content+"</span><span onclick='del("+task_id+")'>&nbsp;&nbsp;<u>del</u></span></div></li>";
        }
        // console.log(string);
        father_node.innerHTML = string;
    }
}

//加载数据函数
function load() {
    var o_todo_task_list = document.getElementById("todo_task_list"); //未完成列表ol对象
    var o_finished_task_list = document.getElementById("finished_task_list");//已完成列表ol对象
    var todo_task_count = 0; //未完成任务数量
    var finished_task_count = 0; //已完成任务数量
    task_list = read_data("task_list"); 
    var todo_task_list = [];//未完成任务数组
    var finished_task_list = [];//已完成任务数组
    console.log("todo_task:",todo_task_list);
    console.log("finished_task:",finished_task_list);
    if (task_list){//有数据
        for (task in task_list){ //遍历系统数据
            if (task_list[task].status){ //判断任务是否完成
                finished_task_list.push(task_list[task]);
                create_dom(o_finished_task_list, finished_task_list);
                finished_task_count++;
            }else {
                todo_task_list.push(task_list[task]);
                create_dom(o_todo_task_list, todo_task_list);
                todo_task_count++;
            }
        }
    }else {
        console.log("没有待办和已办任务。。。");
    }
    document.getElementById("todo_task_count").innerText = todo_task_count;
    document.getElementById("finished_task_count").innerText = finished_task_count;

}
//刷新界面
function reload() {
    window.location.reload();
}

//按状态清除数据
function clear_data(status) {
    console.log(status);
    var task_list = read_data("task_list");
    for (var task_id in task_list){
        if (task_list[task_id].status == status){
            // task_list.splice(task,1); //删除元素
            delete task_list[task_id];
        }
    }
    save_data("task_list",task_list);
    // load()
}
//添加任务
function add() {
    task_list = read_data("task_list");
    var task_id = Date.now(); //给任务添加唯一编号)
    var task_content = document.getElementById("task_content");
    var task_content_value = task_content.value.replace(/^\s+|\s+$/g,"");//获取任务内容,并去两边空格
    if (!task_content_value){
        alert("任务是空！");
        return;
    }
    var new_task = {};
    new_task.task_id = task_id;
    new_task.task_content = task_content_value;
    new_task.status = false; //默认是false，未完成
    // task_list.push(new_task); //将新增任务插入到队列中
    task_list[task_id] = new_task; //将新增任务插入到队列中
    console.log("保存");
    task_content.value = ""; //清空表单
    save_data("task_list", task_list);
    // reload(); //刷新界面

}
function update_status(task_id, status) {
    var task_list = read_data("task_list");
    task_list[task_id].status = !status;
    console.log(task_id, status);
    console.log(task_id,task_list[task_id].status);
    save_data("task_list",task_list);
    // load();
}

// function edit(task_id) {
//     new_content = document.getElementById("new-content");
//     new_content_value = new_content.value.replace(/^\s+|\s+$/g,"");
//     if (!new_content_value){
//         alert("修改后任务不能为空！")
//         return;
//     }
//     var task_list = read_data("task_list");
//     console.log(task_list[task_id].task_content);
//     console.log("edit");
// }

function del(task_id) {
    var task_list = read_data("task_list");
    console.log(task_id);
    delete task_list[task_id];
    save_data("task_list", task_list);
}
function  edit(task_id) {
    task_list = read_data("task_list");
    document.getElementById('edit-task-content').style.display = "block";
    document.getElementById("fide").style.display="block";
    document.getElementById("old-content").value = document.getElementById("span_"+task_id).innerText;
    // document.getElementById("submit-content").onclick = edit(task_id);

    document.getElementById("submit-edit").onclick = function(){
        new_content = document.getElementById("new-content");
        new_content_value = new_content.value.replace(/^\s+|\s+$/g,"");
        if (!new_content_value){
            alert("新值不能为空！");
            return;
        }
        task_list[task_id].task_content = new_content_value;
        new_content.value = "";
        save_data("task_list", task_list);
        // document.getElementById("span_"+task_id).innerText = new_content_value;
        // console.log(new_content_value);
        // document.getElementById('edit-task-content').style.display = "none";
        // document.getElementById("fide").style.display="none";
    };
    document.getElementById("console-edit").onclick = function () {
        document.getElementById('edit-task-content').style.display = "none";
        document.getElementById("fide").style.display="none";

    };

}
