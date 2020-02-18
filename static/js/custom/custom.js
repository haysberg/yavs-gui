function jsping(){
    text = document.getElementById("pinginput").value
    document.location = "/ping/" + text
    print("/ping/" + text)
}

function jsportscan(){
    text = document.getElementById("portscaninput").value
    document.location = "/portscan/" + text
    print("/portscan/" + text)
}