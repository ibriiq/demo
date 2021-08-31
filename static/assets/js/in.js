$("document").ready(function () {
    $("#in_claim_missing").on("change", function (e) {




        function toast_question(){
            
            iziToast.question({
                timeout: 20000,
                close: false,
                overlay: true,
                displayMode: 'once',
                id: 'question',
                zindex: 999,
                title: 'Remove Claim missing',
                icon: '',
                position: 'center',
                timeout: false,
                drag: false,
                backgroundColor: "white",
                maxWidth: "30%",
                "min-height": "279%",
                inputs: [
                    ['<label style="position: relative;top: 39px; left: -150px; "> Callsub </label>'],
                    ['<input type=text value=7022730 autofocus style="position: relative;top: 39px; left: -110px; ">']
                ],
                buttons: [
                    ['<button style="position: relative;top: 55px; left: 68px; "><b>Cancel</b></button>', function (instance, toast) {

                        instance.hide({ transitionOut: 'fadeOut' }, toast, 'button');
                        

                    }, true],
                    ['<button style="position: relative;top: 55px; left: 88px; ">Remove claim missing</button>', function (instance, toast) {

                       

                    }],
                ],
               
            });
        }

        
        let blacklist;
        if ($(this).prop('checked')) {
            blacklist = 1;

            toast_question()


        } else {
            blacklist = 0;

            toast_question()
        }
    })
})