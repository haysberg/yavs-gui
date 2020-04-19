function jsping(){
    text = document.getElementById("pinginput").value
    var change = document.getElementById("ping_button");
    change.innerHTML = "Sending ICMP Requests to " + text + "...";
    document.location = "/ping/" + text
    print("/ping/" + text)
}

function jsportscan(){
    text = document.getElementById("portscaninput").value
    var change = document.getElementById("portscan_button");
    change.innerHTML = "Scanning " + text + " for open ports...";
    document.location = "/portscan/" + text
    print("/portscan/" + text)
}

function jsservicescan(){
    text = document.getElementById("servicescaninput_fqdn").value
    var change = document.getElementById("svcscan_button");
    change.innerHTML = "Scanning Services on " + text + "...";
    document.location = "/servicescan/" + text + "/" + document.getElementById("servicescaninput_ports").value
    print("/portscan/" + text)
}

function jscipherscan(){
    text = document.getElementById("cipherscaninput").value
    var change = document.getElementById("cipher_button");
    change.innerHTML = "Checking Cipher-Suites on " + text + "...";
    document.location = "/cipherscan/" + text
    print("/cipherscan/" + text)
}

function jssubdomains(){
    text = document.getElementById("subscaninput").value
    var change = document.getElementById("subscan_button");
    change.innerHTML = "Scanning (" + text + ") subdomains...";
    document.location = "/subdomains/" + text
    print("/subdomains/" + text)
}

function jssetapi(){
    text = document.getElementById("api-url").value
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", "/setapi/" + text, false ); // false for synchronous request
    xmlHttp.send( null );
    document.getElementById("api-url").value = "API Endpoint URL set !"
}

function jswebscan(){
    text = document.getElementById("webscaninput").value
    var change = document.getElementById("webscan_button");
    change.innerHTML = "Scanning (" + text;
    document.location = "/webappscan/" + text
    print("/webappscan/" + text)
}

function jsdbscan(){
    text = document.getElementById("dbscaninput").value
    text = text.replace(/\//g, "*");
    text = text.replace(/\?/g, "@");
    var change = document.getElementById("dbscan_button");
    change.innerHTML = "Scanning ...";
    document.location = "/databasescan/" + text
    print("/databasescan/" + text)
}