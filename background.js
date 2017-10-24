function onCreated() {
    if (browser.runtime.lastError) {
        console.log(`Error: ${browser.runtime.lastError}`);
    } else {
        console.log("Item created successfully");
    }
}

function onError(error) {
    console.log(`Error: ${error}`);
}

function onSuccess(success){

}

browser.menus.create({
    id: "tts",
    title: "Text-to-speach",
    contexts: ["selection"]
}, onCreated);
  

browser.menus.onClicked.addListener((info, tab) => {
    switch (info.menuItemId) {
        case "tts":
            var sending = browser.runtime.sendNativeMessage("selectionToSpeech", info.selectionText);
            sending.then(onSuccess, onError);
        break;
    }
});