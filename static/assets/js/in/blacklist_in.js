$("document").ready(function () {
    //blacklist xaliye 
    $(document).on("click", "#in_blacklist", function () {

        callsub = $("#callsub").val()

        // in_blacklist

        swal({
            title: "Are you sure?",
            text: `you want remove Blacklist status of callsub ${callsub} !!!`,
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
            .then((willDelete) => {
                if (willDelete) {


                    $.ajax({
                        url: "IN/iCBSWebBlacklist",
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
                    swal("Removing Blacklist is cancled");
                }
            });






    });


});