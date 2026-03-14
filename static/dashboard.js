
async function scan(){

let username = document.getElementById("username").value

let r = await fetch("/username",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({username:username})

})

let data = await r.json()

document.getElementById("username_result").innerText = data.result

}



async function shodan(){

let ip = document.getElementById("ip").value

let r = await fetch("/shodan",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({ip:ip})

})

let data = await r.json()

document.getElementById("shodan_result").innerText = JSON.stringify(data,null,2)

}



async function domain(){

let domain = document.getElementById("domain").value

let r = await fetch("/domain",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({domain:domain})

})

let data = await r.json()

document.getElementById("domain_result").innerText = JSON.stringify(data,null,2)

}



async function generateReport(){

let data = document.getElementById("username_result").innerText

let r = await fetch("/report",{

method:"POST",

headers:{"Content-Type":"application/json"},

body:JSON.stringify({data:data})

})

let result = await r.json()

document.getElementById("report").innerText = result.report

         }
