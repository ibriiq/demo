
// UpdateXallyeBlacklist 

$("#UpdateXallyeBlacklist").on("submit", function (e) {
    e.preventDefault()

    //Validation for callsub begins here
    if ($("#callsub").val() == "") {
        $("#callsub").addClass("is-invalid");
        $("#errorforcallsub").text("Please enter your callsub");
        e.stopPropagation()
        return false
    }
    else {
        $("#callsub").removeClass("is-invalid");
        $("#callsub").addClass("is-valid");
        $("#errorforcallsub").text("");
    }//Validation for callsub ends here


    
    //Validation for xaliye_status begins here
    if ($("#xaliye_status").val() == "") {
        $("#xaliye_status").addClass("is-invalid");
        $("#errorforxaliye_status").text("Please enter your xaliye_status");
        e.stopPropagation()
        return false
    }
    else {
        $("#xaliye_status").removeClass("is-invalid");
        $("#xaliye_status").addClass("is-valid");
        $("#errorforxaliye_status").text("");
    }//Validation for xaliye_status ends here



    //Validation for description begins here
    if ($("#description").val() == "") {
        $("#description").addClass("is-invalid");
        $("#errorfordescription").text("Please enter your description");
        e.stopPropagation()
        return false
    }
    else {
        $("#description").removeClass("is-invalid");
        $("#description").addClass("is-valid");
        $("#errorfordescription").text("");
    }//Validation for username ends here


    $.ajax({
        url: $(this).attr("action"),
        method: $(this).attr("method"),
        data: new FormData(this),
        dataType: "json",
        processData: false,
        contentType: false,
        success: function (resp) {
            console.log(resp);
            if (resp.success) {
                iziToast.success({
                    title: 'Xaliye blacklist sucessfull',
                    message: resp.msg,
                    position: 'topRight',
                });
             
            } else {
                iziToast.error({
                    title: 'Login failed',
                    message: resp.msg,
                    position: 'topRight',
                });

                $("#login_btn").attr("disabled", false);
                $("#login_btn").html(`Log In`);
            }
        }
    });



})
    // UpdateXallyeBlacklist
