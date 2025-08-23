
function getCSRFToken() {
        return document.querySelector('[name=csrfmiddlewaretoken]').value;
}


function addTask() {
    let taskInfo = document.getElementById("task").value;
    let date = document.getElementById("date").value;
    let important = document.getElementById("important").checked;
    let completed = document.getElementById("completed").checked;
    let url = "/daily/add_task/";

    fetch(url, {
        method: "POST",
        headers: {
            'X-CSRFToken': getCSRFToken(),
            'X-Requested-With': 'XMLHttpRequest',
        },
        body: JSON.stringify({
            task: taskInfo,
            date: date,
            important: important,
            completed: completed
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Site responded:", data);
        loadTasks();
        resetFields();
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function resetFields() {
    document.getElementById("task").value = "";
    document.getElementById("date").value = "";
    document.getElementById("important").checked = false;
    document.getElementById("completed").checked = false;
}

function loadTasks() {
    fetch("/daily/get_task/", {
        method: "GET",
        headers: {
            'X-Requested-With': 'XMLHttpRequest',
        }
    })
    .then(res => res.json())
    .then(data => {
        const list = document.getElementById('task-list');
        list.innerHTML = ""
        if (data.tasks.length == 0) {
            list.innerHTML = "<p>No tasks created yet.</p>";
            return;
        }

        data.tasks.forEach(task => {
            const div = document.createElement('div');
            div.className = "task-bubble";
            div.setAttribute("data-id", task.taskid);
            div.innerHTML = `
                    ${task.taskid} - ${task.task} (${task.date}) - Important: ${task.important} - Completed: ${task.completed} <button class="delete-button" onclick='deleteTask(this);'><img src="/static/icon/trash.png"></button>

            `;
            div.style.opacity = 0;
            list.appendChild(div);
            setTimeout(() => div.style.opacity = 1, 200);
        });
    })
    .catch(error => console.error("Error Loading Tasks:", error));
}

window.onload = function () {
    loadTasks();
};

function deleteTask(elem) {
   const taskBubble = elem.closest('.task-bubble');
   const taskId = taskBubble.getAttribute('data-id');
   console.log('Identified taskid:', taskId);

   fetch("/daily/delete_task/", {
    method: "POST",
    headers: {
        'X-CSRFToken': getCSRFToken(),
        "X-Requested-With": 'XMLHttpRequest'
    },
    body: JSON.stringify({
        'taskid': taskId
    })
   })
   .then(res => res.json())
   .then(data  => {
    console.log("Deleted TaskID", taskId);
    console.log(data);
   });

   const taskRemove = document.querySelector(`.task-bubble[data-id='${taskId}']`);
   if (taskRemove) {
    taskRemove.remove();
   }
}
