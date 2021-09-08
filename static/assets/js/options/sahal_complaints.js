$("document").ready(function() {
    $("#toggle_sahal_complaints_model").on("click", function() {

        $("#sahal_complaints_model").find("input,select").val('')
        $("#sahal_complaints_model").find("input,select").removeClass("is-valid is-invalid")

        $("#SaveSahalComp_btn").attr("disabled", false)
        $("#SaveSahalComp_btn").html(`Save`)

        $("#sahal_complaints_model").modal("show")
    })

    $("#callsub_sahal_comp").on("blur", function() {
        if ($("#callsub_sahal_comp").val() != '') {
            if ($("#callsub_sahal_comp").val().length == 7) {
                $("#callsub_sahal_comp").removeClass("is-invalid")
                $("#callsub_sahal_comp").addClass("is-valid")
                $("#errorforcallsub_sahal_comp").text("")
                $.ajax({
                    url: "options/DisplayPhoneDirectory",
                    method: 'post',
                    data: {
                        "search_by": "Number",
                        "search_value": $("#callsub_sahal_comp").val(),
                    },
                    dataType: "json",
                    success: function(resp) {
                        if (resp.success) {
                            $("#Custname_sahal_comp").val(resp.data[0].DicName)
                            $("#Custname_sahal_comp").removeClass("is-invalid")
                            $("#Custname_sahal_comp").addClass("is-valid")
                        }
                    }
                });
            } else {
                $("#callsub_sahal_comp").addClass("is-invalid")
                $("#errorforcallsub_sahal_comp").text("please insert correct number ")
                $("#Custname_sahal_comp").val('')
                $("#Custname_sahal_comp").removeClass("is-valid")
                $("#Custname_sahal_comp").addClass("is-invalid")
            }
        }
    })


    $("#SaveSahalComp").on("submit", function(e) {
        $("#SaveSahalComp_btn").attr("disabled", true)
        $("#SaveSahalComp_btn").html(`<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`)
        e.preventDefault()
        form_isvalid = false;


        //Validation for callsub begins here
        if ($("#callsub_sahal_comp").val() == "") {
            $("#callsub_sahal_comp").addClass("is-invalid");
            $("#errorforcallsub_sahal_comp").text("Please enter your callsub");
            form_isvalid = true
        } else {
            $("#callsub_sahal_comp").removeClass("is-invalid");
            $("#callsub_sahal_comp").addClass("is-valid");
            $("#errorforcallsub_sahal_comp").text("");
        } //Validation for callsub ends here


        //Validation for comptype begins here
        if ($("#comptype").val() == "") {
            $("#comptype").addClass("is-invalid");
            $("#errorforcomptype").text("Please enter your complaint type");
            form_isvalid = true
        } else {
            $("#comptype").removeClass("is-invalid");
            $("#comptype").addClass("is-valid");
            $("#errorforcomptype").text("");
        } //Validation for comptype ends here


        //Validation for Center begins here
        if ($("#Center").val() == "") {
            $("#Center").addClass("is-invalid");
            $("#errorforCenter").text("Please enter your complaint type");
            form_isvalid = true
        } else {
            $("#Center").removeClass("is-invalid");
            $("#Center").addClass("is-valid");
            $("#errorforCenter").text("");
        } //Validation for Center ends here


        //Validation for reciever begins here
        if ($("#reciever").val() == "") {
            $("#reciever").addClass("is-invalid");
            $("#errorforreciever").text("Please enter your reciever");
            form_isvalid = true
        } else if ($("#reciever").val().length != 7) {
            $("#reciever").addClass("is-invalid");
            $("#errorforreciever").text("Please enter correct number");
            form_isvalid = true
        } else {
            $("#reciever").removeClass("is-invalid");
            $("#reciever").addClass("is-valid");
            $("#errorforreciever").text("");
        } //Validation for reciever ends here


        //Validation for amount begins here
        if ($("#amount").val() == "") {
            $("#amount").addClass("is-invalid");
            $("#errorforamount").text("Please enter your complaint type");
            form_isvalid = true
        } else {
            $("#amount").removeClass("is-invalid");
            $("#amount").addClass("is-valid");
            $("#errorforamount").text("");
        } //Validation for amount ends here


        if (form_isvalid) {
            e.stopPropagation()
            $("#SaveSahalComp_btn").attr("disabled", false)
            $("#SaveSahalComp_btn").html(`Save`)
            return false
        }

        $.ajax({
            url: $(this).attr("action"),
            method: $(this).attr("method"),
            data: new FormData(this),
            dataType: "json",
            processData: false,
            contentType: false,
            success: function(resp) {
                if (resp.success) {
                    iziToast.success({
                        title: 'Sahal complaint',
                        message: resp.msg,
                        position: 'topRight',
                    });

                    $("#sahal_complaints_model").modal("hide")

                } else {
                    iziToast.error({
                        title: 'Sahal complaint',
                        message: resp.msg,
                        position: 'topRight',
                    });
                    $("#SaveSahalComp_btn").attr("disabled", false)
                    $("#SaveSahalComp_btn").html(`Save`)
                }
            }
        });


    })

});