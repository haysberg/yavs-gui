function jsping(){
    text = document.getElementById("pinginput").value
    document.location = "/ping/" + text
    print("/ping/" + text)
}