
$('#light-button').on('click', function(event) {
    console.log("light button click");
    var button = $('#light-button');
    if (button.text() === "Turn light on") {
        $.ajax({
            url: "/light_on",
            data: {},
            type: "post",
            success: function(response) {
                button.text(function() {return "Turn light off"});
                button.removeClass("btn-info");
                button.addClass("btn-dark");

                console.log("turn light on");
                console.log(response);
            },
            failure: function(response) {
                console.log("failed to turn light on:");
                console.log(response);
            }
        });
    } else if (button.text() === "Turn light off") {
        $.ajax({
            url: "light_off",
            data: {},
            type: "post",
            success: function(response) {
                button.text(function() {return "Turn light on"});
                button.removeClass("btn-dark");
                button.addClass("btn-info");

                console.log("turn light off");
                console.log(response);
            },
            failure: function(response) {
                console.log("failed to turn light off:");
                console.log(response);
            }
        })
    }
});