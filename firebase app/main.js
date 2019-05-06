var mainApp = {};

(function(){
    var firebase = app_firebase;
    var uid = null;
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
          // User is signed in.
          uid = user.uid;
        }else{
            uid=null;
            window.location.replace('login.html');
        }
      });  
      function logOut(){
        firebase.auth().signOut();
        window.location.replace('login.html');
      
      }
      
      function messageHandler(err){
        if(!!err){
          console.log(err);
        }else{
          console.log('success');
        }
      }
      function fnCreate(){
        //console.log(user);
        var path = "users/"+uid;
        var email = app_firebase.auth().password.email;
        console.log(email);
        data = p_game.data;
        console.log(data);
        var data = {
          email: email,
          data: data
        }
        app_firebase.databaseApi.create(path, data, messageHandler);
      }
      mainApp.logOut = logOut;
      mainApp.Create = fnCreate;
})()
