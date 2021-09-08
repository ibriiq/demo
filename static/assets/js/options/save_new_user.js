$("document").ready(function() {
    $("#toggle_save_new_user_model").on("click", function() {
        $("#save_new_user_model").find("input,select").val('')
        $("#save_new_user_model").find("input,select").removeClass("is-valid is-invalid")

        $("#SaveNewUsers_btn").attr("disabled", false)
        $("#SaveNewUsers_btn").html(`Save`)

        $("#save_new_user_model").modal("show")
    })

    $("#callsub_new_user").on("blur", function() {
        if ($("#callsub_new_user").val() != '') {
            if ($("#callsub_new_user").val().length == 7) {
                $("#callsub_new_user").removeClass("is-invalid")
                $("#callsub_new_user").addClass("is-valid")
                $("#errorforcallsub_new_user").text("")
                $.ajax({
                    url: "options/DisplayPhoneDirectory",
                    method: 'post',
                    data: {
                        "search_by": "Number",
                        "search_value": $("#callsub_new_user").val(),
                    },
                    dataType: "json",
                    success: function(resp) {
                        if (resp.success) {
                            $("#name_save_new_user").val(resp.data[0].DicName)
                            $("#name_save_new_user").removeClass("is-invalid")
                            $("#name_save_new_user").addClass("is-valid")
                        }
                    }
                });
            } else {
                $("#callsub_new_user").addClass("is-invalid")
                $("#errorforcallsub_new_user").text("please insert correct number ")
                $("#name_save_new_user").val('')
                $("#name_save_new_user").removeClass("is-valid")
                $("#name_save_new_user").addClass("is-invalid")
            }
        }
    })


    $("#SaveNewUsers").on("submit", function(e) {
        $("#SaveNewUsers_btn").attr("disabled", true)
        $("#SaveNewUsers_btn").html(`<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`)
        e.preventDefault()
        form_isvalid = false;


        //Validation for callsub begins here
        if ($("#callsub_new_user").val() == "") {
            $("#callsub_new_user").addClass("is-invalid");
            $("#errorforcallsub_new_user").text("Please enter your callsub");
            form_isvalid = true
        } else {
            $("#callsub_new_user").removeClass("is-invalid");
            $("#callsub_new_user").addClass("is-valid");
            $("#errorforcallsub_new_user").text("");
        } //Validation for callsub ends here


        //Validation for Name begins here
        if ($("#name_save_new_user").val() == "") {
            $("#name_save_new_user").addClass("is-invalid");
            $("#errorforname_save_new_user").text("Please enter callsub so that the name could be found automatically");
            form_isvalid = true
        } else {
            $("#name_save_new_user").removeClass("is-invalid");
            $("#name_save_new_user").addClass("is-valid");
            $("#errorforname_save_new_user").text("");
        } //Validation for Name ends here


        //Validation for Group begins here
        if ($("#Group").val() == "") {
            $("#Group").addClass("is-invalid");
            $("#errorforGroup").text("Please enter your Group");
            form_isvalid = true
        } else {
            $("#Group").removeClass("is-invalid");
            $("#Group").addClass("is-valid");
            $("#errorforGroup").text("");
        } //Validation for Group ends here


        //Validation for dept begins here
        if ($("#dept").val() == "") {
            $("#dept").addClass("is-invalid");
            $("#errorfordept").text("Please enter your department");
            form_isvalid = true
        } else {
            $("#dept").removeClass("is-invalid");
            $("#dept").addClass("is-valid");
            $("#errorfordept").text("");
        } //Validation for dept ends here


        //Validation for Center begins here
        if ($("#Center_save_new_user").val() == "") {
            $("#Center_save_new_user").addClass("is-invalid");
            $("#errorforCenter_save_new_user").text("Please enter your center");
            form_isvalid = true
        } else {
            $("#Center_save_new_user").removeClass("is-invalid");
            $("#Center_save_new_user").addClass("is-valid");
            $("#errorforCenter_save_new_user").text("");
        } //Validation for Center ends here


        //Validation for UserID begins here
        if ($("#UserID").val() == "") {
            $("#UserID").addClass("is-invalid");
            $("#errorforUserID").text("Please enter your UserID");
            form_isvalid = true
        } else {
            $("#UserID").removeClass("is-invalid");
            $("#UserID").addClass("is-valid");
            $("#errorforUserID").text("");
        } //Validation for UserID ends here


        //Validation for UserName begins here
        if ($("#UserName").val() == "") {
            $("#UserName").addClass("is-invalid");
            $("#errorforUserName").text("Please enter your UserName");
            form_isvalid = true
        } else {
            $("#UserName").removeClass("is-invalid");
            $("#UserName").addClass("is-valid");
            $("#errorforUserName").text("");
        } //Validation for UserName ends here

        //Validation for status_save_new_user begins here
        if ($("#status_save_new_user").val() == "") {
            $("#status_save_new_user").addClass("is-invalid");
            $("#errorforstatus_save_new_user").text("Please enter your status");
            form_isvalid = true
        } else {
            $("#status_save_new_user").removeClass("is-invalid");
            $("#status_save_new_user").addClass("is-valid");
            $("#errorforstatus_save_new_user").text("");
        } //Validation for status_save_new_user ends here


        //Validation for ViewBalGroup begins here
        if ($("#ViewBalGroup").val() == "") {
            $("#ViewBalGroup").addClass("is-invalid");
            $("#errorforViewBalGroup").text("Please enter your ViewBalGroup");
            form_isvalid = true
        } else {
            $("#ViewBalGroup").removeClass("is-invalid");
            $("#ViewBalGroup").addClass("is-valid");
            $("#errorforViewBalGroup").text("");
        } //Validation for ViewBalGroup ends here

        //Validation for CerUserID begins here
        if ($("#CerUserID").val() == "") {
            $("#CerUserID").addClass("is-invalid");
            $("#errorforCerUserID").text("Please enter your CerUserID");
            form_isvalid = true
        } else {
            $("#CerUserID").removeClass("is-invalid");
            $("#CerUserID").addClass("is-valid");
            $("#errorforCerUserID").text("");
        } //Validation for CerUserID ends here





        if (form_isvalid) {
            e.stopPropagation()
            $("#SaveNewUsers_btn").attr("disabled", false)
            $("#SaveNewUsers_btn").html(`Save`)
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
                        title: 'Register user',
                        message: resp.msg,
                        position: 'topRight',
                    });

                    $("#save_new_user_model").modal("hide")

                } else {
                    if (resp.status == 408) {
                        $("#UserID").addClass("is-invalid");
                        $("#errorforUserID").text(resp.msg);
                        $("#UserID").focus()
                        $("#SaveNewUsers_btn").attr("disabled", false)
                        $("#SaveNewUsers_btn").html(`Save`)
                    } else if (resp.status == 409) {
                        $("#UserName").addClass("is-invalid");
                        $("#errorforUserName").text(resp.msg);
                        $("#UserName").focus()
                        $("#SaveNewUsers_btn").attr("disabled", false)
                        $("#SaveNewUsers_btn").html(`Save`)
                    } else {
                        iziToast.error({
                            title: 'Register user',
                            message: resp.msg,
                            position: 'topRight',
                        });
                        $("#SaveNewUsers_btn").attr("disabled", false)
                        $("#SaveNewUsers_btn").html(`Save`)
                    }
                }
            }
        });


    })

});