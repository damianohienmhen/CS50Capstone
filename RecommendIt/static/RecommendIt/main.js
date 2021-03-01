console.log("Sanity check!");

function edit(id) { 

fetch(`/edit/${id}`)
.then(response => response.json())
.then(edit => {

 r =     `<form enctype="multipart/form-data" onsubmit="submit(${edit.id})" action ="/submit/${edit.commentid}" method ="POST" >
          <input type='hidden' name='csrfmiddlewaretoken' value="${ csrftoken }"/>
          <input type="text" name = "updatepost" class="form-control" id="compose-body" placeholder="Body" value="${edit.new_comment}" ></input>
          <button type="submit" name= "update" value ="update" class="btn btn-primary">Update</button>
          </form>`;

document.querySelector(`#thecomment_${edit.commentid}`).innerHTML =  r;


function submit(id) { 

fetch(`/submit/${id}`)
.then(response => response.json())
.then(comment => {

document.querySelector(`#thepost_${comment.commentid}`).innerHTML =  `<div id = "thepost_${comment.id}" class="containerborder">
    				                                                  <div style="font-size:30px;">${comment.user}</div>
    				    											  <br>
                    												  ${comment.new_comment}<br>
                   													  </div>`;
console.log(comment)


})
}; 



})
};

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
