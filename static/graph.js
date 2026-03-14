
var nodes = new vis.DataSet([
{ id:1,label:"Target"},
{ id:2,label:"Email"},
{ id:3,label:"IP"},
{ id:4,label:"Domain"}
])

var edges = new vis.DataSet([
{from:1,to:2},
{from:1,to:3},
{from:1,to:4}
])

var container = document.getElementById("network")

var data = {nodes:nodes,edges:edges}

new vis.Network(container,data,{})
