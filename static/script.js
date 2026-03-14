async function usernameSearch(){

let username = document.getElementById("username").value

let r = await fetch("/username",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({username:username})

})

let data = await r.json()

document.getElementById("username-result").innerText = data.result

}



async function askAI(){

let question = document.getElementById("ai-question").value

let r = await fetch("/ai",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({question:question})

})

let data = await r.json()

document.getElementById("ai-result").innerText = data.reply

}



async function loadThreats(){

let r = await fetch("/threats")

let data = await r.json()

document.getElementById("threats").innerText = JSON.stringify(data,null,2)

}
