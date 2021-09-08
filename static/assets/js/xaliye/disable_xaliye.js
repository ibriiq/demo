$("document").ready(function(){
    //Disable xaliye starts here

    // xaliye_disable
    $(document).on("click", "#xaliye_disable", function () {
        $("#callsub_disable").removeClass("is-invalid");
        $("#callsub_disable").removeClass("is-valid");
        // $("#callsub_disable").val("");
        $("#errorforcallsub_disable").text("")

        $("#description_disable").removeClass("is-invalid");
        $("#description_disable").removeClass("is-valid");
        $("#description_disable").val("");
        $("#errorfordescription_disable").text("");


        $("#xaliye_status_disable").val("");
        $("#xaliye_status_disable").removeClass("is-valid");
        $("#xaliye_status_disable").removeClass("is-invalid");

      
        $("#disable_xaliye_model").modal("show")

    });

    // UpdateXallyeDisable 
    $("#UpdateXallyeDisable").on("submit", function (e) {
        e.preventDefault()
        let isblacklisted = "";

        if ($("#xaliye_status_disable").val() == "1") {
            isblacklisted = "Enabled"
            addcssclass = "btn-outline-success"
            removecssclass = "btn-outline-danger"
        }
        else {
            isblacklisted = "Disabled"
            addcssclass = "btn-outline-danger"
            removecssclass = "btn-outline-success"
        }


        //Validation for callsub_disable begins here
        if ($("#callsub_disable").val() == "") {
            $("#callsub_disable").addClass("is-invalid");
            $("#errorforcallsub_disable").text("Please enter your callsub");
            e.stopPropagation()
            return false
        }
        else {
            $("#callsub_disable").removeClass("is-invalid");
            $("#callsub_disable").addClass("is-valid");
            $("#errorforcallsub_disable").text("");
        }//Validation for callsub ends here



        //Validation for xaliye_status_disable begins here
        if ($("#xaliye_status_disable").val() == "") {
            $("#xaliye_status_disable").addClass("is-invalid");
            $("#errorforxaliye_status_disable").text("Please select xaliye status");
            e.stopPropagation()
            return false
        }
        else {
            $("#xaliye_status_disable").removeClass("is-invalid");
            $("#xaliye_status_disable").addClass("is-valid");
            $("#errorforxaliye_status_disable").text("");
        }//Validation for xaliye_status ends here

        //Validation for description begins here
        if ($("#description_disable").val() == "") {
            $("#description_disable").addClass("is-invalid");
            $("#errorfordescription_disable").text("Please enter your description");
            e.stopPropagation()
            return false
        }
        else {
            $("#description_disable").removeClass("is-invalid");
            $("#description_disable").addClass("is-valid");
            $("#errorfordescription_disable").text("");
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

                    $("#xaliye_disable").html(isblacklisted)
                    $("#xaliye_disable").removeClass(removecssclass)
                    $("#xaliye_disable").addClass(addcssclass)
                    // cssclass
                    $("#disable_xaliye_model").modal("hide")

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
    // UpdateXallyeDisable

//Disable xaliye ends here
})