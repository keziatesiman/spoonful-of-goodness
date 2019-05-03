function uncheckAntiVegan() {
    $("#id_contains_egg").prop("checked", false);
    $("#id_contains_meat").prop("checked", false);
    $("#id_contains_pork").prop("checked", false);
    $("#id_contains_fish").prop("checked", false);
    $("#id_contains_milk").prop("checked", false);
}

function uncheckVegan() {
    $("#id_is_vegan").prop("checked", false);
}

function uncheckMilk() {
    $("#id_contains_milk").prop("checked", false);
}

function uncheckMilkSubstitute() {
    $("#id_contains_milk_substitute").prop("checked", false);
}

function milkIsChecked() {
    uncheckVegan();
    uncheckMilkSubstitute();
}