document.forms['add-activity']['xp'].value = 0;

function add25() {
    var xp = document.forms['add-activity']['xp'].value;
    var intxp =  parseInt(xp);
    var total = intxp + 25;
    document.forms['add-activity']['xp'].value = total;
}

function add50() {
    var xp = document.forms['add-activity']['xp'].value;
    var intxp =  parseInt(xp);
    var total = intxp + 50;
    document.forms['add-activity']['xp'].value = total;
}

function add75() {
    var xp = document.forms['add-activity']['xp'].value;
    var intxp =  parseInt(xp);
    var total = intxp + 75;
    document.forms['add-activity']['xp'].value = total;
}

function add100() {
    var xp = document.forms['add-activity']['xp'].value;
    var intxp =  parseInt(xp);
    var total = intxp + 100;
    document.forms['add-activity']['xp'].value = total;
}

function renull() {
    document.forms['add-activity']['xp'].value = 1-1;
}