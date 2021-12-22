function val() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var p1 = document.getElementById("p1").value;
    var p2 = document.getElementById("p2").value;
    var error = document.getElementById("error_message");
    var text;
    error.style.padding = "10px";
    if (name.length < 6) {
        text = "Name Should be more than 6 characters";
        error.innerHTML = text;
        return false;
    }
    if (email.indexOf("@") == -1 || email.length < 6) {
        text = "Your email is invalid.";
        error_message.innerHTML = text;
        return false;
    }
    if (p1.length < 8) {
        text = "Password Should be more than 8 characters";
        error.innerHTML = text;
        return false;
    }
    if (p1 != p2) {
        text = "Password does not match";
        error.innerHTML = text;
        return false;
    }
    function ValidatePassword() {
        var regex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$@!%&*?])[A-Za-z\d#$@!%&*?]{10,12}$/;
        var txt = document.getElementById("textbox1");
        if (!regex.test(p1)) {
            alert("Password strength is not good.");
        } else {
            alert("Password strength is good.");
        }
    }
    var frm = document.getElementById("form");
    frm.style.display = 'none';
    var hid = document.getElementById("h2");
    hid.style.display = 'none';
    var disp = document.getElementById("h21");
    disp.style.display = 'block';
    error.style.padding = "0px";
    return false;
}
