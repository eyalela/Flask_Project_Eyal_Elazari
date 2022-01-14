function get_users(num){
    fetch(`https://reqres.in/api/users/${num}`).then(
        response => response.json()
    ).then(
        response_obj =>send_users_to_page(response_obj.data)
    ).catch(
        err => console.log(err)
    )
}

function send_users_to_page(response_obj_data){
    const curry_main = document.querySelector("contentassignment11");
    const section = document.createElement('section');
    section.innerHTML = `
        <img src="${response_obj_data.avatar}" alt="profile pic"/>
        <div>
            <span>${response_obj_data.first_name} ${response_obj_data.last_name}</span>
            <br>
            <a href="mailto:${response_obj_data.email}">send email</a>
        </div>
        `;
    curry_main.appendChild(section);
}


function show_as_json() {
    console.log("validation")
    let display = document.getElementById("show_as_json");
    if (display.style.display === "none") {
        display.style.display = "block";
    } else {
        display.style.display = "none";
    }
}