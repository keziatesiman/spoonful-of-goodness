function getHrefForPlannerCardButton(elm) {
    var hrefElementContainer = elm.parentElement;
    var collectionsOfElm = hrefElementContainer.childNodes;
    console.log(collectionsOfElm);
    for (i = 0; i < collectionsOfElm.length; i++) {
        if (collectionsOfElm[i].nodeName == "H5") {
            var url = "/foodList/" + collectionsOfElm[i].innerHTML;
            console.log('Set href ' + url);
            elm.href = url;
        }
    }
}