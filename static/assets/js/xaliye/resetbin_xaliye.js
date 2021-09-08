$("document").ready(function(){
    //Reset xaliye bin start here



// xaliye_disable
$(document).on("click", "#xaliye_resetbin", function () {
    alert("Resetbin")
    $("#callsub_disable").removeClass("is-invalid");
    $("#callsub_disable").removeClass("is-valid");
    // $("#callsub_disable").val("");
    $("#errorforcallsub_disable").text("")

    $("#description_disable").removeClass("is-invalid");
    $("#description_disable").removeClass("is-valid");
    $("#description_disable").val("");
    $("#errorfordescription_disable").text("");


    $("#resetbin").val("");
    $("#resetbin").removeClass("is-valid");
    $("#resetbin").removeClass("is-invalid");

  
    $("#resetbin_xaliye_model").modal("show")

});


// UpdateXallyeresetbin 
$("#UpdateXallyeresetbin").on("submit", function (e) {
    e.preventDefault()
    let isblacklisted = "";

    if ($("#xaliye_status_resetbin").val() == "1") {
        isblacklisted = "Enabled"
        addcssclass = "btn-outline-success"
        removecssclass = "btn-outline-danger"
    }
    else {
        isblacklisted = "resetbind"
        addcssclass = "btn-outline-danger"
        removecssclass = "btn-outline-success"
    }


    //Validation for callsub_resetbin begins here
    if ($("#callsub_resetbin").val() == "") {
        $("#callsub_resetbin").addClass("is-invalid");
        $("#errorforcallsub_resetbin").text("Please enter your callsub");
        e.stopPropagation()
        return false
    }
    else {
        $("#callsub_resetbin").removeClass("is-invalid");
        $("#callsub_resetbin").addClass("is-valid");
        $("#errorforcallsub_resetbin").text("");
    }//Validation for callsub ends here



    //Validation for resetbin begins here
    if ($("#resetbin").val() == "") {
        $("#resetbin").addClass("is-invalid");
        $("#errorforresetbin").text("Please select xaliye status");
        e.stopPropagation()
        return false
    }
    else if($("#resetbin").val().length > 4 || $("#resetbin").val().length < 4 )
    {
        $("#resetbin").addClass("is-invalid");
        $("#errorforresetbin").text("Please make sure reset bin is 4 digits");
        e.stopPropagation()
        return false
    }
    else {
        $("#resetbin").removeClass("is-invalid");
        $("#resetbin").addClass("is-valid");
        $("#errorforresetbin").text("");
    }
    
    
    //Validation for resetbin ends here


    //Validation for description begins here
    if ($("#description_resetbin").val() == "") {
        $("#description_resetbin").addClass("is-invalid");
        $("#errorfordescription_resetbin").text("Please enter your description");
        e.stopPropagation()
        return false
    }
    else {
        $("#description_resetbin").removeClass("is-invalid");
        $("#description_resetbin").addClass("is-valid");
        $("#errorfordescription_resetbin").text("");
    }//Validation for username ends here


    $.ajax({
        url: $(this).attr("action"),
        method: $(this).attr("method"),
        data: new FormData(this),
        dataType: "json",
        processData: false,
        contentType: false,
        success: function (resp) {
            // console.log(resp);
            if (resp.success) {
                iziToast.success({
                    title: 'Xaliye status update sucessfull',
                    message: resp.msg,
                    position: 'topRight',
                });

                $("#xaliye_resetbin").html(isblacklisted)
                $("#xaliye_resetbin").removeClass(removecssclass)
                $("#xaliye_resetbin").addClass(addcssclass)
                // cssclass
                $("#resetbin_xaliye_model").modal("hide")

                // btn-outline-danger

            } else {
                iziToast.error({
                    title: 'Xaliye status update failed',
                    message: resp.msg,
                    position: 'topRight',
                });
            }
        }
    });
})
// UpdateXallyeresetbin




//Reset xaliye bin ends here
})