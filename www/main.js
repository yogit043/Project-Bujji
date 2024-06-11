let mm = 0
// var audio = document.getElementById("bg")
// audio.volume = 0.2
$(document).ready(function() {
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#MicBtn").click(function () { 
        mm = mm+1
        // audio.pause()
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        if(mm==1){
        eel.wish()
        }
        else{
            eel.wish1()
        }
        eel.allCommands()()
        // audio.play()
        // eel.takecommand()()
    });

    function doc_keyUp(e) {
        // if (e.metaKey && e.key === 'b' ) {  // Changed from metaKey to ctrlKey
        //     eel.playAssistantSound()
        //     $("#Oval").attr("hidden", true);
        //     $("#SiriWave").attr("hidden", false);
        //     eel.allCommands()();
        // }
        
        if (e.altKey && e.key === 'b') {  // Changed from metaKey to altKey
            mm = mm+1
            // audio.pause()
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            if(mm==1){
            eel.wish()
            }
            else{
                eel.wish1()
            }
            eel.allCommands()();
            // audio.play()
        }
    }
    document.addEventListener('keyup',doc_keyUp,false)

    function PlayAssistant(message){
        if(message!=""){
            $("#Oval").attr('hidden',true)
            $("#SiriWave").attr('hidden',false)
            eel.allCommands(message)
            $("#chatbot").val("")
            $("#MicBtn").attr('hidden',false)
            $("#SendBtn").attr('hidden',true)
        }
    }

    function ShowHideButton(message) {
        if(message.length==0){
            $("#MicBtn").attr('hidden',false)
            $("#SendBtn").attr('hidden',true)
        }
        else{
            $("#MicBtn").attr('hidden',true)
            $("#SendBtn").attr('hidden',false)
        }
      }

    $("#chatbot").keyup(function(){
        let message = $("#chatbot").val()
        ShowHideButton(message)
    })

    $("#SendBtn").click(function(){
        let message = $("#chatbot").val()
        PlayAssistant(message)
    })
    $("#chatbot").keypress(function(e){
        key = e.which
        if(key==13){
            let message = $("#chatbot").val()
            
            PlayAssistant(message)
        }
    })
});


