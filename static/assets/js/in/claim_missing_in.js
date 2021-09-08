$("document").ready(function () {
    //blacklist xaliye 
    $(document).on("click", "#in_claim_missing", function () {


        // in_claim_missing

        callsub = $("#callsub").val()

        swal({
            title: "Are you sure?",
            text: `you want remove claim missing status of callsub ${callsub} !!!`,
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
            .then((willDelete) => {
                if (willDelete) {


                    $.ajax({
                        url: "IN/iCBSWebdisClaimMissing",
                        method: 'post',
                        data: {
                            "callsub": $("#callsub").val(),
                        },
                        dataType: "json",
                        success: function (resp) {
                            console.log(resp);
                            if (resp.success) {
                                swal(resp.msg, {
                                    icon: "success",
                                });
                                // $("#Custname_sahal_comp").val(resp.data[0].DicName)
                            } else {
                                swal(resp.msg, {
                                    icon: "error",
                                });
                            }
                        }
                    });


                } else {
                    swal("Removing missingclaim is cancled");
                }
            });






    });


});