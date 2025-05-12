$("#first_select").on("dblclick", function () {
    const elem = $(this).find("option:selected").remove().clone();
    $("#second_select").append(elem);
});

$("#second_select").on("dblclick", function () {
    const elem = $(this).find("option:selected").remove().clone();
    $("#first_select").append(elem);
});
