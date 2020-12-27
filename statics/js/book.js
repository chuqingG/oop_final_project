
var bookInfoKey = ['Name', 'BookID', 'ISBN', 'Publisher', 'Date', 'Author', 'Tag','Stock']
var bookInfoKeyScale = {'Name': "15%", 'BookID': "15%",
    'ISBN': "10%", 'Publisher': "20%", 'Date': "10%",
    'Author': "10%", 'Tag': "10%",'Stock': "10%"}
var userInfoKey = ['Name', 'UserID', 'Type', 'PhoneNumber']
var userInfoKeyScale = {'Name': "25%", 'UserID': "25%",
    'Type': "25%", 'PhoneNumber': "25%"}
booklist = []
userlist = []

function listbook() {
    $("#fileTable").children("*").remove();
    fileTable = $("#fileTable")
    
    for(var i = 0; i < booklist.length; i++) {
        tr = $("<tr>")
        for(var key of bookInfoKey) {
            var td = $(`<td id = ${key}></td>`)
                .addClass("mytd")
                .text(booklist[i][key])
                .width(bookInfoKeyScale[key])
                .css("font-size", "12px")
                .css("background-color", "#ffffd9")
                .css("border", "1px solid black")
            tr.append(td)
        }
        
        fileTable.append(tr)
    }
    console.log(fileTable)
}

function listuser() {
    $("#userTable").children("*").remove();
    userTable = $("#userTable")
    
    for(var i = 0; i < userlist.length; i++) {
        tr = $("<tr>")
        for(var key of userInfoKey) {
            var td = $(`<td id = ${key}></td>`)
                .addClass("mytd")
                .text(userlist[i][key])
                .width(userInfoKeyScale[key])
                .css("font-size", "12px")
                .css("background-color", "#ffffd9")
                .css("border", "1px solid black")
            tr.append(td)
        }
        userTable.append(tr)
    }
    console.log(userTable)
}

function listhis() {
    $("#hisTable").children("*").remove();
    hisTable = $("#hisTable")
    
    for(var i = 0; i < hislist.length; i++) {
        tr = $("<tr>")
        var td = $(`<td id = ${"History"}></td>`)
            .addClass("mytd")
            .text(hislist[i])
            .width("100%")
            .css("font-size", "12px")
            .css("background-color", "#ffffd9")
            .css("border", "1px solid black")
        tr.append(td)
        hisTable.append(tr)
    }
    console.log(hisTable)
}

function listcur() {
    $("#curTable").children("*").remove();
    curTable = $("#curTable")
    
    for(var i = 0; i < curlist.length; i++) {
        tr = $("<tr>")
        var td = $(`<td id = ${"CurrentBorrow"}></td>`)
            .addClass("mytd")
            .text(curlist[i])
            .width("100%")
            .css("font-size", "12px")
            .css("background-color", "#ffffd9")
            .css("border", "1px solid black")
        tr.append(td)
        curTable.append(tr)
    }
    console.log(curTable)
}