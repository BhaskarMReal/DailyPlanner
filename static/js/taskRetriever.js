
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
        console.log("Site responded:", data)
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
