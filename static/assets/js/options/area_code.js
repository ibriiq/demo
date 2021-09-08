$("document").ready(function () {
    $("#toggle_area_code_model").on("click", function () {

        $("#area_code_model").modal("show")
    })

    $("#DisplayArea").on("submit", function (e) {
        $("#area_code_search_btn").attr("disabled", true)
        $("#area_code_search_btn").html(`<span class="spinner-grow spinner-grow-sm" role="status" aria-hidden="true"></span>`)
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
                                        ${resp.Countcode}
                                    </td>
                                    <td>
                                        ${resp.Countname}
                                    </td>
                                </tr>
                            ` });


                    $("#area_code_search_btn").html("Search")
                    $("#area_code_search_btn").attr("disabled", false)
                    $("#table_body_area_code").html(body)

                } else {
                    body =
                        `
                            <tr>
                                <td colspan='5' style='text-align: center;'> No Data is found </td>
                            </tr>
                        `

                    $("#area_code_search_btn").html("Search")
                    $("#area_code_search_btn").attr("disabled", false)
                    $("#table_body_area_code").html(body)
                }
            }
        });
    })

})