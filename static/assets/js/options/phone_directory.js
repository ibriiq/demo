$("document").ready(function () {
    $("#toggle_phone_directroy_model").on("click", function () {
        $("#phone_directory_model").modal("show")
    })

    $("#DisplayPhoneDirectory").on("submit", function (e) {
        $("#phone_directory_search_btn").attr("disabled", true)
        $("#phone_directory_search_btn").html(`<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`)
        e.preventDefault()
        $.ajax({
            url: $(this).attr("action"),
            method: $(this).attr("method"),
            data: new FormData(this),
            dataType: "json",
            processData: false,
            contentType: false,
            success: function (resp) {
                if (resp.success) {
                    let body = ''
                    $.each(resp.data, function (index, resp) {
                        body +=
                            `
                                <tr>
                                    <td>
                                        ${resp.DicCallsub}
                                    </td>
                                    <td>
                                        ${resp.DicName}
                                    </td>
                                    <td>
                                        ${resp.DicAddress}
                                    </td>
                                    <td>
                                        ${resp.DicCentre}
                                    </td>
                                    <td>
                                        ${resp.DicStartDate}
                                    </td>
                                </tr>
                            `
                    });

                    $("#phone_directory_search_btn").html("Search")
                    $("#phone_directory_search_btn").attr("disabled", false)
                    $("#table_body_phone_directory").html(body)
                } else {
                    if (resp.status == 401) {
                        body =
                            `
                                <tr>
                                    <td colspan='5' style='text-align: center;'> 
                                        <div class="alert alert-danger" style="width: 50%; margin: 0 auto; text-align: center;">
                                            <i class="fas fa-exclamation-circle"></i> Authorization has been denied for this request.
                                        </div>
                                    
                                    </td>
                                </tr>
                            `
                    }
                    else {
                        body =
                            `
                                <tr>
                                    <td colspan='5' style='text-align: center;'> No Data is found </td>
                                </tr>
                            `
                    }

                    $("#phone_directory_search_btn").html("Search")
                    $("#phone_directory_search_btn").attr("disabled", false)
                    $("#table_body_phone_directory").html(body)
                }
            }
        });
    })

})


