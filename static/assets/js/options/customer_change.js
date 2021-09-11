$("document").ready(function() {
    $("#toggle_customer_change_model").on("click", function() {

        $("#customer_change_model").find(".empty").val('')
        $("#customer_change_model").find("input,select").removeClass("is-valid is-invalid")

        $("#UpdateCustChange_btn").attr("disabled", false)
        $("#UpdateCustChange_btn").html(`Save`)

        $("#customer_change_model").modal("show")
    })

    $("#UpdateCustChange").on("submit", function(e) {
        $("#UpdateCustChange_btn").attr("disabled", true)
        $("#UpdateCustChange_btn").html(`<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`)
        e.preventDefault()
        form_isvalid = false;


        //Validation for callsub begins here
        if ($("#callsub_customer_change").val() == "") {
            $("#callsub_customer_change").addClass("is-invalid");
            $("#errorforcallsub_customer_change").text("Please enter your callsub");
            form_isvalid = true
        } else if ($("#callsub_customer_change").val().length != 7) {
            $("#callsub_customer_change").addClass("is-invalid");
            $("#errorforcallsub_customer_change").text("Please enter correct number");
            form_isvalid = true
        }else {
            $("#callsub_customer_change").removeClass("is-invalid");
            $("#callsub_customer_change").addClass("is-valid");
            $("#errorforcallsub_customer_change").text("");
        } //Validation for callsub ends here


        //Validation for Descrip begins here
        if ($("#Descrip").val() == "") {
            $("#Descrip").addClass("is-invalid");
            $("#errorforDescrip").text("Please enter your complaint type");
            form_isvalid = true
        } else {
            $("#Descrip").removeClass("is-invalid");
            $("#Descrip").addClass("is-valid");
            $("#errorforDescrip").text("");
        } //Validation for Descrip ends here


        //Validation for TranType begins here
        if ($("#TranType").val() == "") {
            $("#TranType").addClass("is-invalid");
            $("#errorforTranType").text("Please enter your complaint type");
            form_isvalid = true
        } else {
            $("#TranType").removeClass("is-invalid");
            $("#TranType").addClass("is-valid");
            $("#errorforTranType").text("");
        } //Validation for TranType ends here




        //Validation for CGS begins here
        if ($("#CGS").val() == "") {
            $("#CGS").addClass("is-invalid");
            $("#errorforCGS").text("Please enter your complaint type");
            form_isvalid = true
        } else {
            $("#CGS").removeClass("is-invalid");
            $("#CGS").addClass("is-valid");
            $("#errorforCGS").text("");
        } //Validation for CGS ends here


        if (form_isvalid) {
            e.stopPropagation()
            $("#UpdateCustChange_btn").attr("disabled", false)
            $("#UpdateCustChange_btn").html(`Save`)
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
                        title: 'Customer change',
                        message: resp.msg,
                        position: 'topRight',
                    });

                    $("#customer_change_model").modal("hide")

                } else {
                    iziToast.error({
                        title: 'Customer change',
                        message: resp.msg,
                        position: 'topRight',
                    });
                    $("#UpdateCustChange_btn").attr("disabled", false)
                    $("#UpdateCustChange_btn").html(`Save`)
                }
            }
        });


    })

});