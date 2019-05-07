var mainApp = {};

(function(){
    var firebase = app_firebase;
    var uid = null;
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
          // User is signed in.
          uid = user.uid;
          console.log(uid);
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
        var database = firebase.database();
        var ref = database.ref('players/'+uid);
        
        var data = {
            name : "deep",
            score : "45"
        }
        ref.set(data);

      }
      mainApp.logOut = logOut;
      mainApp.fnCreate = fnCreate;
})()
