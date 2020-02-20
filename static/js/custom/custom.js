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

function jsservicescan(){
    text = document.getElementById("servicescaninput_fqdn").value
    document.location = "/servicescan/" + text + "/" + document.getElementById("servicescaninput_ports").value
    print("/portscan/" + text)
}