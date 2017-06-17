var names_list = []


function add_name(name) {
    str =  '<div class="name" id="name' + name.id + '">'
        + '<p>' + name.name + ' | '
        + '<a onclick="deleteName(' + name.id + ', \'' + name.name + '\')">delete</a>'
        + '</p>'
        + '</div>'
    return str;
}

function add_winner(name) {
    str = '<div class="winner" id="winner' + name.id + '">'
        + '<h3>' + name.name + '</h3>'
        + '</div>'
    return str;
}



$(document).ready(function () {
    getNames();
})


function deleteName(id, name) {
    $.ajax({
        type: "POST",
        url: "/delete/",
        data: JSON.stringify({ id: id}),
        success: function () {
            $('#name'+id).remove();
            names_list.pop(name)
        },
        error: function (data) {
            console.log(data);
        }
    })
}

function addName() {
    var name = $("#inputName").val();
    // var patt = new RegExp("^test$");
    var patt = new RegExp("^\\w{3,30}$");
    if (!patt.test(name)) {
        $('#status').empty().append("name must consist 3-30 chars of a-z, A-Z, 0-9, _");
        return false;
    }


    if (names_list.includes(name)) {
        $('#status').empty().append("Name already exists");
        return false;
    }

    $.ajax({
        type: "POST",
        url: "/add/",
        data: JSON.stringify({ name: name}),
        success: function (data) {
            names_container = $('#namesList');
            item = JSON.parse(data).name;
            names_container.append(add_name(item))
            names_list.push(item.name);

        },
        error: function (data) {
            console.log(data);
        }
    })


}

function getWinners(){
    $.ajax({
        type: "GET",
        url: "/winners/",
        success: function (data) {
            winners_container = $('#winnersList').empty();
            JSON.parse(data).names.forEach(function (item, i, names) {
                winners_container.append(add_winner(item))
            })
        }
    })
}

function getNames(){
    $.ajax({
        type: "GET",
        url: "/names/",
        success: function (data) {
            names_container = $('#namesList');
            JSON.parse(data).names.forEach(function (item, i, names) {
                names_container.append(add_name(item))
                names_list.push(item.name);
            })
        }
    })
}