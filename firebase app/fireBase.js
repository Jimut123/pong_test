var app_firebase = {};

(function(){
    // Initialize Firebase
    var config = {
        apiKey: "AIzaSyD-YkuZamopwNX_581fFobGefywR-LiOc8",
        authDomain: "pongai-d6660.firebaseapp.com",
        databaseURL: "https://pongai-d6660.firebaseio.com",
        projectId: "pongai-d6660",
        storageBucket: "pongai-d6660.appspot.com",
        messagingSenderId: "1051076549691"
    };
    firebase.initializeApp(config);

    app_firebase = firebase;
    
    function fnCreate(path, body, callBack){
        
        if(!path || !body) return
        app_firebase.database().ref(path).set(body, callBack);

    }

    app_firebase.databaseApi = {
        create: fnCreate,
        // read: fnRead,
        // update : fnUpdate,
        // delete: fnDelete
    }

})()