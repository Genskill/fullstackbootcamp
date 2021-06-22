function handleUpdate(resp) {
    $("#details").html(resp);
}
function handleClick(event) {
    var link = event.target;
    console.log(link['href']);
    $.get(link).done(handleUpdate);
    event.preventDefault();
    }
function main() {
    $("a.joblink").click(handleClick);
}
$(main);
