$("document").ready(function(){
     //blacklist xaliye 
     $(document).on("click", "#xaliye_blacklist", function () {
        $("#callsub").removeClass("is-invalid");
        $("#callsub").removeClass("is-valid");
        // $("#callsub").val("");
        $("#errorforcallsub").text("")

        $("#description").removeClass("is-invalid");
        $("#description").removeClass("is-valid");
        $("#description").val("");
        $("#errorfordescription").text("");


        $("#xaliye_status").val("");
        $("#xaliye_status").removeClass("is-valid");
        $("#xaliye_status").removeClass("is-invalid");

      
        $("#blacklist_xaliye_model").modal("show")

    });






    // UpdateXallyeBlacklist 
    $("#UpdateXallyeBlacklist").on("submit", function (e) {
        e.preventDefault()
        let isblacklisted = "";

        if ($("#xaliye_status").val() == "1") {
            isblacklisted = "Blacklisted"
            addcssclass = "btn-outline-danger"
            removecssclass = "btn-outline-success"
        }
        else {
            isblacklisted = "Not blacklisted"
            addcssclass = "btn-outline-success"
            removecssclass = "btn-outline-danger"

        }


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
                // console.log(resp);
                if (resp.success) {
                    iziToast.success({
                        title: 'Xaliye blacklist sucessfull',
                        message: resp.msg,
                        position: 'topRight',
                    });

                    $("#blacklist_xaliye_model").modal("hide")
                    $("#xaliye_blacklist").html(isblacklisted)
                    $("#xaliye_blacklist").removeClass(removecssclass)
                    $("#xaliye_blacklist").addClass(addcssclass)
                    // cssclass

                    // btn-outline-danger

                } else {
                    iziToast.error({
                        title: 'Xaliye blacklist failed',
                        message: resp.msg,
                        position: 'topRight',
                    });
                }
            }
        });



    })
    // UpdateXallyeBlacklist

     //blacklist xaliye 
})